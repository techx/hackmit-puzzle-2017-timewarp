import string

def caesar_char(c, key):
    isupper =  c.isupper()
    c = c.lower()
    index = string.ascii_lowercase.find(c) 
    if index == -1:
        return c
        
    c = string.ascii_lowercase[(index + key) % 26]
        
    return c.upper() if isupper else c 

def caesar(s, key):
    cipher = ""
    for c in s:
        cipher += caesar_char(c, key) 
    return cipher 
    
PLAINTEXT = "decrypted.html"
CIPHERTEXT = "index.html"

with open(PLAINTEXT) as fin:
    with open(CIPHERTEXT) as fout:
        for line in fin:
            

