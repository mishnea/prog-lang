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
    def test(cls, s):
        return cls.re.fullmatch(s)

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


class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.word = ""
        self.potential_types = token_types

    def push_token(self, token):
        # Append token
        self.tokens.append(token)
        # Reset
        self.word = ""
        self.potential_types = token_types

    def push(self, c):
        self.word += c
        print(c, self.word)
        new_types = []
        for token_type in self.potential_types:
            # Narrow down token types
            if token_type.test(self.word):
                new_types.append(token_type)
        if len(new_types) == 1:
            token_type = new_types[0]
            token = token_type(self.word)
            self.push_token(token)
            return
        if new_types:
            # Continue same word
            self.potential_types = new_types
            return
        if len(self.word) == 1:
            # Reset if single character doesn't match anything
            self.word = ""
            self.potential_types = token_types
            return
        # Push token using previous word
        token_type = self.potential_types[0]
        token = token_type(self.word[:-1])
        self.push_token(token)
        # Try last char again
        return self.push(c)

    def flush(self):
        if not self.word:
            return
        token_type = self.potential_types[0]
        token = token_type(self.word)
        self.push_token(token)


tokenizer = Tokenizer()

for c in text:
    tokenizer.push(c)
tokenizer.flush()

print(tokenizer.tokens)

stack = []
for token in tokenizer.tokens:
    token.exec(stack)
