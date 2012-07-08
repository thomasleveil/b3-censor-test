import sys, os, site

this_dir = os.path.dirname(__file__)

# if you created a virtualenv named 'env'
ALLDIRS = [os.path.join(this_dir, 'env/lib/python2.7/site-packages')]

# Remember original sys.path.
prev_sys_path = list(sys.path)

# Add each new site-packages directory.
for directory in ALLDIRS:
    site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

# add out application to the sys path
sys.path.insert(0, os.path.join(this_dir, 'app'))
os.chdir(this_dir)

from b3censortest import app as application # This loads your application
