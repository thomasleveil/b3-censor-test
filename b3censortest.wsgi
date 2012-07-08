import sys, os, bottle

this_dir = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(this_dir, 'app'))
os.chdir(this_dir)

import b3censortest # This loads your application

application = bottle.default_app()
