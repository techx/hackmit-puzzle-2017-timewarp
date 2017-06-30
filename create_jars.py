import os
import jinja2
import struct
import subprocess
import shutil

from hashing import *

TEMPLATE = jinja2.Environment(loader=jinja2.FileSystemLoader('./')).get_template('WarpCLI.java.j2')

for i in range(255 + 1):
    answer = date_for_i(i)
    epoch_s = 365*24*60*60*i
    r = TEMPLATE.render({'answer': answer, 'start_epoch': epoch_s})
    with open('WarpCLI.java', 'w') as f:
        f.write(r)
    subprocess.call(['javac', 'WarpCLI.java'])
    name = file_for_i(i)
    subprocess.call(['jar', 'cvfe', 'WarpCLI.jar', 'WarpCLI', 'WarpCLI.class'])
    shutil.move('WarpCLI.jar', 'jars/%s' % name)

# Clean up clean up
os.remove('WarpCLI.java')
os.remove('WarpCLI.class')
