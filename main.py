import re


fname = "input.txt"

with open(fname) as f:
    text = f.read()


class Token:
    re = re.compile('.*')
    
    @classmethod
    def test(cls, s):
        return cls.re.fullmatch(s)


class Identifier(Token):
    re = re.compile('[a-zA-Z]\\w*')


class Number(Token):
    re = re.compile('[0-9]+(\\.[0-9]+)?')


class String(Token):
    re = re.compile('\"[^"]*\"')


class Tokenizer:
    def __init__(self):
        tokens = []
        current = ''

    def push(self, c):

    


for c in text:
    
