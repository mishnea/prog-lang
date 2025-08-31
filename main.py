import re


fname = "input.txt"

with open(fname) as f:
    text = f.read()


token_types = []


def register_token_type(cls):
    token_types.append(cls)
    return cls


class Token:
    re = re.compile(".*")

    @classmethod
    def consume(cls, s):
        m = cls.re.match(s)
        if m:
            return cls(m[0]), s[m.end() :]
        return None, s

    def __repr__(self):
        return f'{type(self).__name__}: "{self.word}"'

    def __init__(self, word):
        self.word = word

    def exec(self, stack):
        pass


@register_token_type
class Log(Token):
    re = re.compile("log")

    def exec(self, stack):
        print(stack[-1])


@register_token_type
class Identifier(Token):
    re = re.compile("[a-zA-Z]\\w*")


@register_token_type
class Number(Token):
    re = re.compile("[0-9]+(\\.[0-9]+)?")

    def exec(self, stack):
        stack.append(float(self.word))


@register_token_type
class String(Token):
    re = re.compile('"[^"]*"')

    def exec(self, stack):
        stack.append(self.word)


@register_token_type
class Add(Token):
    re = re.compile("\\+")

    def exec(self, stack):
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)


@register_token_type
class Whitespace(Token):
    re = re.compile("\\s+")


tokens = []
while text:
    for token_type in token_types:
        token, text = token_type.consume(text)
        if token:
            tokens.append(token)
            break
    else:
        raise ValueError(f"Cannot parse text:\n{text}")

print(tokens)

stack = []
for token in tokens:
    token.exec(stack)
