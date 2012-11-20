B3 Censor plugin online tester
==============================

This projects provides a website that aims to help users of BigBrotherBot (B3) to configure the Censor plugin.
The Censor plugin has one of the most difficult configuration file of the B3 project and hopefully this website will
help users avoid configuration errors and reduce the time required to add and test new badword and badname rules.


Test it live
------------

http://b3-censor-test.cucurb.net



Installation
------------

### Requirements

- [python 2.7](www.python.org)
- [flask](http://pypi.python.org/pypi/Flask/)
- [mock](http://pypi.python.org/pypi/mock/)
- [b3](http://pypi.python.org/pypi/b3/)


This project has been tested on a [virtualenv](http://pypi.python.org/pypi/virtualenv/) with :
- Python 2.7.3
- Flask==0.9
- Jinja2==2.6
- Werkzeug==0.8.3
- argparse==1.2.1
- b3==1.8.2
- mock==0.8.0
- wsgiref==0.1.2


### Virtualenv setup

Follow the commands below to install the website in directory /var/www/b3-censor-plugin/

    mkdir /var/www/b3-censor-test
    cd /var/www/b3-censor-test

    # get the files
    wget https://github.com/thomasleveil/b3-censor-test/zipball/master -O b3-censor-test.zip
    mv courgette-b3-censor-test-e2c36e4/* .
    rm -r courgette-b3-censor-test-e2c36e4/

    # create a virtualenv and install dependencies
    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt

    # test the website
    python app/b3censortest.py

If all those steps are followed you can test the website connecting to http://127.0.0.1:5000



### Apache2 webserver configuration

This website can run under Apache2 with the mod_wsgi module.
Refer to the doc/apache_vhost.conf file for an example of Apache2 virtualhost configuration.



References
----------

- BigBrotherBot: http://www.bigbrotherbot.net
- Censor plugin documentation: http://wiki.bigbrotherbot.net/usage:censor_plugin
