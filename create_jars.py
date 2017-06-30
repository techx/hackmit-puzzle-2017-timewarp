import os
import jinja2
import struct
import subprocess
import shutil
import random

from hashing import *
from subprocess import PIPE, Popen

TEMPLATE = jinja2.Environment(loader=jinja2.FileSystemLoader('./')).get_template('WarpCLI.java.j2')

random.seed(1337)

for i in range(255 + 1):
    answer = date_for_i(i)
    epoch_s = random.randint(631152000, 2208988800)

    # From https://github.com/shamanland/simple-string-obfuscator
    p = Popen(['java', 'SimpleStringObfuscator', "You got it, the answer is: {}".format(answer)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    exitcode = p.returncode

    obf = output.decode('utf-8')

    print(epoch_s)

    r = TEMPLATE.render({'obf': obf, 'start_epoch': epoch_s})
    with open('WarpCLI.java', 'w') as f:
        f.write(r)
    subprocess.call(['javac', 'WarpCLI.java'])
    name = file_for_i(i)
    subprocess.call(['jar', 'cvfe', 'WarpCLI.jar', 'WarpCLI', 'WarpCLI.class', 'WarpCLI$1.class'])
    shutil.move('WarpCLI.jar', 'jars/%s' % name)

# Clean up clean up
os.remove('WarpCLI.java')
os.remove('WarpCLI.class')
os.remove('WarpCLI$1.class')
