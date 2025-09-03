import re


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
        return f"{type(self).__name__}: {repr(self.word)}"

    def __init__(self, word):
        self.word = word

    def eval(self, stack):
        pass


@register_token_type
class Log(Token):
    re = re.compile("log")

    def eval(self, stack):
        print(stack[-1])


@register_token_type
class Identifier(Token):
    re = re.compile("[a-zA-Z]\\w*")

    map = {}

    @classmethod
    def assign(cls, name, value):
        cls.map[name] = value

    def eval(self, stack):
        stack.append(self.map[self.word])


@register_token_type
class Number(Token):
    re = re.compile("[0-9]+(\\.[0-9]+)?")

    def eval(self, stack):
        stack.append(float(self.word))


@register_token_type
class String(Token):
    re = re.compile('"[^"]*"')

    def eval(self, stack):
        stack.append(self.word[1:-1])


@register_token_type
class Add(Token):
    re = re.compile("\\+")

    def eval(self, stack):
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)


@register_token_type
class Assignment(Token):
    re = re.compile("=")

    def eval(self, stack):
        value = stack.pop()
        name = stack.pop()
        Identifier.assign(name, value)


@register_token_type
class Whitespace(Token):
    re = re.compile("\\s+")
