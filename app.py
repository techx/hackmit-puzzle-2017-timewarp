'''
    Did someone say single file apps?
'''

from bs4 import BeautifulSoup, NavigableString
from cipher import cipher
from config import *
import hashlib

from flask import (
    Flask,
    render_template_string,
    render_template,
    send_from_directory,
    redirect
)

app = Flask(__name__)


'''
    Utils
'''

def get_num_jars():
    return len(glob.glob(os.path.join('./jars/', "*.jar")))

def get_jar_uuid(username):
    return hashlib.sha256(username + SECRET + ANOTHER_SECRET).hexdigest()

def shift_map(username):
    return int(hashlib.sha256(username + SECRET).hexdigest(), 16) % 23 + 2 # Not 0 or 26

'''
    Routes
'''

@app.route("/")
def index():
    return render_template("awk.html")

@app.route("/u/<username>/suchsecret/<id>")
def jar_file(username, id):
    if not get_jar_uuid(username) == id:
        return "Bad ID", 400

    # FIXME Agree on a hash scheme with pat
    jar_file_index = int(hashlib.sha256(username + SECRET).hexdigest(), 16) % get_num_jars()
    return send_from_directory("jars", "jar_{}.json".format(jar_file_index))


@app.route("/u/<username>")
def alien_view(username):
    # Calculate shift
    shift = shift_map(username)

    # Calculate JAR url
    jar_id = get_jar_uuid(username)

    jar_url="{domain}/u/{username}/suchsecret/{id}".format(
                                        domain=DOMAIN,
                                        username=username,
                                        id=jar_id
                                      )
    jar_url = cipher(jar_url, shift)

    # Read the decrypted html file
    with open('templates/decrypted.html') as f:
        html_doc = f.read()

    # Pass it through jinja
    html_doc = render_template_string(html_doc.decode('utf-8', 'ignore'), jar_url=jar_url)

    # Init parser
    soup = BeautifulSoup(html_doc, 'lxml')

    # Iterate through every element and replace the inner text with cipher
    for element in soup.findAll():
        for index, sub_element in enumerate(element.contents):
            if type(sub_element) == NavigableString:
                element.contents[index].replace_with(cipher(element.contents[index].strip(), shift))

    # Render it in browser
    return soup.prettify(formatter=None)

'''
    Flask debugger
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)