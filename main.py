import sys

from tokenizer import Tokenizer

try:
    fname = sys.argv[1]
except IndexError:
    print("Provide input filename")
    exit(0)

with open(fname) as f:
    text = f.read()

tokenizer = Tokenizer(text)

tokens = tokenizer.tokenize()

print(*tokens, sep="   ")
