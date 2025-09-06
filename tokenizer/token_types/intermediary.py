import re

from .token import Token
from ..tokenizer import Tokenizer


@Tokenizer.add_type
class Whitespace(Token):
    re = re.compile("\\s+")


@Tokenizer.add_type
class Equals(Token):
    re = re.compile("=")


@Tokenizer.add_type
class Add(Token):
    re = re.compile("\\+")


@Tokenizer.add_type
class Identifier(Token):
    re = re.compile("[a-zA-Z]\w*")
