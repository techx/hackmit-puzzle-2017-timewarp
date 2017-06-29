'''
    Cipher provider. Provides a common interface to cipher things
'''

import string

def caesar_char(c, key):
    isupper =  c.isupper()
    c = c.lower()
    index = string.ascii_lowercase.find(c) 
    if index == -1:
        return c
        
    c = string.ascii_lowercase[(index + key) % 26]
        
    return c.upper() if isupper else c 

'''
    Currently implements a Caesar Cipher
'''
def cipher(s, key):
    cipher = ""
    for c in s:
        cipher += caesar_char(c, key) 
    return cipher 


