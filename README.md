B3 Censor plugin online tester
==============================

This projects provides a website that aims to help users of BigBrotherBot (B3) to configure the Censor plugin.
The Censor plugin has one of the most difficult configuration file of the B3 project and hopefully this website will help users avoid configuration errors and reduce the time required to add and test new badword rules.


Test it live
------------

http://b3-censor-test.cucurb.net



Installation
------------

### Requirements

- [python 2.7](www.python.org)
- [flask](http://pypi.python.org/pypi/Flask/)
- [b3](http://pypi.python.org/pypi/b3/)


This project has been tested on a [virtualenv](http://pypi.python.org/pypi/virtualenv/) with :
- Python 2.7.3
- Flask==0.9
- Jinja2==2.6
- Werkzeug==0.8.3
- argparse==1.2.1
- b3==1.8.2
- wsgiref==0.1.2


### Apache2 webserver configuration

This website can run under Apache2 with the mod_wsgi module.
Refer to the doc/apache_vhost.conf file for an example of Apache2 virtualhost configuration.



References
----------

- BigBrotherBot: http://www.bigbrotherbot.net
- Censor plugin documentation: http://wiki.bigbrotherbot.net/usage:censor_plugin
