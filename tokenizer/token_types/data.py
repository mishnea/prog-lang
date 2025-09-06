import re
from .token import Token
from ..tokenizer import Tokenizer


@Tokenizer.add_type
class String(Token):
    re = re.compile('".*?"')


@Tokenizer.add_type
class Number(Token):
    re = re.compile("-?([1-9]\\d*|0)(\\.\\d+)?")
