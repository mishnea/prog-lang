from copy import copy

from .token_types import token_types, Whitespace


def tokenizer(text):
    text = copy(text)
    tokens = []
    while text:
        for token_type in token_types:
            token, text = token_type.consume(text)
            if token:
                if isinstance(token, Whitespace):
                    break
                tokens.append(token)
                break
        else:
            raise ValueError(f"Cannot parse text:\n{text}")
    return tokens
