import json
import string
import pathlib
import random

"""
    key.py - managment of key files
    basicly, a key file contain an random generated string assigned for each letter
    and then we use this key file to encrypt/decrypt inputs
"""

supported_characters = string.digits + string.ascii_letters + string.punctuation + string.whitespace
codestring_characters = string.digits + string.ascii_letters + string.punctuation

class Key:
    def __init__(self, file_name="key.json") -> None:
        self.file_name = file_name
        self.pth = pathlib.Path(self.file_name)
        self.exists = self.pth.exists()
        
    def load(self):
        if self.exists:
            with open(self.file_name, "r") as file:
                file_data = json.load(file)
            
            return file_data
        return False
    
    def generate(self, codestring_length=5):
        if not self.exists:
            file_data = {}
            generated_codeStrings = []

            sep = ""
            for _ in range(codestring_length):
                sep += random.choice(codestring_characters)
            file_data["sep"] = sep
            generated_codeStrings.append(sep)

            for ch in supported_characters:
                
                run = True
                while run:
                    codestring = ""
                    for _ in range(codestring_length):
                        codestring += random.choice(codestring_characters)

                    if not codestring in generated_codeStrings:
                        generated_codeStrings.append(codestring)
                        run = False
                        file_data[ch] = codestring

            with open(self.file_name, "w") as file:
                json.dump(file_data, file)
                return True
        return False
