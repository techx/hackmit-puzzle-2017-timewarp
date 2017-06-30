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
    with open('tmp/WarpCLI.java', 'w') as f:
        f.write(r)
    subprocess.call(['javac', 'tmp/WarpCLI.java'])
    name = file_for_i(i)
    shutil.move('tmp/WarpCLI.class', 'jars/%s' % name)
