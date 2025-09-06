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


@Tokenizer.add_type
class Recall(Token):
    re = re.compile("_")


@Tokenizer.add_type
class Placeholder(Token):
    re = re.compile("\\$")


@Tokenizer.add_type
class Comma(Token):
    re = re.compile(",")


@Tokenizer.add_type
class Lparen(Token):
    re = re.compile("\\(")


@Tokenizer.add_type
class Rparen(Token):
    re = re.compile("\\)")


@Tokenizer.add_type
class Pipe(Token):
    re = re.compile("->")
