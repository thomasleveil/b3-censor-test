# -*- encoding: utf-8 -*-
import logging
import os
from flask import Flask
from flask.globals import request
from flask.templating import render_template
from StringIO import StringIO

app = Flask(__name__)


from b3.config import XmlConfigParser
from b3.plugins.censor import CensorPlugin
from b3.fake import FakeConsole, FakeClient
from b3.functions import minutesStr
from b3.events import VetoEvent
from b3 import __file__ as b3_module__file__

b3log = logging.getLogger('output')

with open(os.path.join(os.path.dirname(b3_module__file__), 'conf/plugin_censor.xml')) as default_config_file:
    default_config_content = default_config_file.read()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():

    b3log_file = StringIO()

    config_log_content = ''
    config_content = None
    chat_text = ''
    chat_consequences = ''

    if request.method == 'POST':

        # create a B3 bot
        b3bot_conf = XmlConfigParser()
        b3bot_conf.loadFromString('<configuration/>')
        b3bot = FakeConsole(b3bot_conf)

        # create a Censor plugin instance
        censor_conf = XmlConfigParser()
        censor_plugin = CensorPlugin(b3bot, censor_conf)

        # create a player Joe to test the chat messages
        joe = FakeClient(console=b3bot, name="Joe", guid="000joe000")

        # monkey patch the Censor plugin penalizeClient method to log its actions
        # and remove a dependy over the admin plugin
        censor_plugin.penalizeClient = penalizeClient

        # add our log handler to collect B3 log messages
        b3log_handler = logging.StreamHandler(b3log_file)
        b3log.addHandler(b3log_handler)

        # read form data
        config_content = request.form['config_content']
        chat_text = request.form['chat']

        if config_content is not None:
            # we got a config to test
            censor_conf.loadFromString(config_content)
            b3log_file.truncate(0)
            b3log.info("--------- loading Censor plugin config ----------")
            censor_plugin.onLoadConfig()
            b3log.info("--------- Censor plugin config loaded ----------")
            b3log_file.seek(0)
            config_log_content = b3log_file.read()
            b3log_file.truncate(0)

            if chat_text is not None:
                # we got some chat to check for badwords
                b3log_file.truncate(0)
                try:
                    censor_plugin.checkBadWord(text=chat_text, client=joe)
                except VetoEvent:
                    pass
                b3log_file.seek(0)
                chat_consequences = b3log_file.read()
                b3log_file.truncate(0)
    else:
        if config_content is None:
            config_content = default_config_content

    return render_template('index.html', config_content=config_content, chat_text=chat_text, log_config=config_log_content, chat_consequences=chat_consequences)


def penalizeClient(penalty, client, data=''):
    """ monkey patch the censor plugin """
    b3log.info("Joe gets penalized with a %s" % penalty.type)
    b3log.info("duration: %s" % minutesStr(penalty.duration))
    b3log.info("reason : %s" % penalty.reason)
    b3log.info("reasonkeyword : %s" % penalty.keyword)

if __name__ == '__main__':
    app.debug = True
    app.run()
