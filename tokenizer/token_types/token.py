class Token:
    re = None

    @classmethod
    def test(cls, text):
        match = cls.re.match(text)
        if match is None:
            return None, text
        word = match[0]
        rest = text[match.end() :]
        return word, rest

    def __repr__(self):
        return f"{type(self).__name__}<{repr(self.word)}>"

    def __init__(self, word):
        self.word = word
