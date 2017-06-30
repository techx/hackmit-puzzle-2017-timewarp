'''
    Did someone say single file apps?
    huy
'''

from bs4 import BeautifulSoup, NavigableString
from cipher import cipher
import hashlib
from hashing import file_for_u 
from config import SECRET

from flask import (
    Flask,
    render_template_string,
    render_template,
    send_from_directory,
    redirect,
    Response
)

app = Flask(__name__)


'''
    Utils
'''

def shift_map(username):
    return (int(hashlib.sha256((username + SECRET).encode('utf8')).hexdigest(), 16) % 23) + 2 # Not 0 or 26

'''
    Routes
'''

@app.route("/")
def index():
    return render_template("awk.html")

# Read the decrypted html file
with open('templates/decrypted.html') as f:
    html_doc = f.read()

@app.route("/u/<username>")
def alien_view(username):
    # Calculate shift
    shift = shift_map(username)

    # Calculate JAR url
    jar_name = file_for_u(username)
    jar_url = "/suchsecret/{jar}".format(jar=jar_name)
    jar_url = cipher(jar_url, shift)


    # Pass it through jinja
    html_doc_rendered = render_template_string(html_doc, jar_url=jar_url)

    # Init parser
    soup = BeautifulSoup(html_doc_rendered, 'lxml')

    # Iterate through every element and replace the inner text with cipher
    for element in soup.findAll():
        for index, sub_element in enumerate(element.contents):
            if type(sub_element) == NavigableString:
                element.contents[index].replace_with(cipher(element.contents[index].strip(), shift))

    # Render it in browser
    return soup.prettify(formatter=None)

