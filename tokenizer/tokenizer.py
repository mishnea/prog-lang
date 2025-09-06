class Tokenizer:
    token_types = []

    @classmethod
    def add_type(cls, token_type):
        cls.token_types.append(token_type)

    def __init__(self, text):
        self.text = text
        self.state = None

    def tokenize(self):
        text = self.text
        tokens = []
        while text:
            for token_type in self.token_types:
                word, rest = token_type.test(text)
                if not word:
                    continue
                token = token_type(word)
                tokens.append(token)
                text = rest
                break
            else:
                print(tokens)
                raise ValueError(f'No token matching text beginning with "{text[:10]}"')
        return tokens
