from tokenizer import tokenizer, token_types

fname = "input.txt"

with open(fname) as f:
    text = f.read()


tokens = tokenizer(text)


print("First pass:", tokens)

for i, token in enumerate(tokens[::-1]):
    j = len(tokens) - i - 1
    if isinstance(token, token_types.Add):
        tokens[j], tokens[j + 1] = tokens[j + 1], tokens[j]
    if isinstance(token, token_types.Assignment):
        tokens[j], tokens[j + 1] = tokens[j + 1], tokens[j]

print("Second pass:", tokens)

stack = []
for token in tokens:
    token.eval(stack)
