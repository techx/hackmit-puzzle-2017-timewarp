from cipher import cipher
import hashlib

from flask import Flask, render_template_string, render_template
from bs4 import BeautifulSoup, NavigableString
app = Flask(__name__)

SECRET = 'ilikesnails'

@app.route("/")
def index():
    return "Ugh. Awkward. Are u sure u're at the right place?"

def shift_map(username):
    return int(hashlib.sha256(username + SECRET).hexdigest(), 16) % 23 + 2 # Not 0 or 26

@app.route("/u/<username>")
def alien_view(username):
    # Calculate shift
    shift = shift_map(username)

    # Read the decrypted html file
    with open('templates/decrypted.html') as f:
        html_doc = f.read()

    # Pass it through jinja
    html_doc = render_template_string(html_doc.decode('utf-8', 'ignore'))

    # Init parser
    soup = BeautifulSoup(html_doc, 'lxml')

    # Iterate through every element and replace the inner text with cipher
    for element in soup.findAll():
        for index, sub_element in enumerate(element.contents):
            if type(sub_element) == NavigableString:
                element.contents[index].replace_with(cipher(element.contents[index].strip(), shift))

    # Render it in browser
    return soup.prettify(formatter=None)

# Run the flask debug server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)