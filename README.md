## How to

Edit input.txt, then `python main.py`.

prog-lang.example is basically unrelated and none of that will work

Token types are defined in `tokenizer/token_types.py`. It is pretty easy to understand.

## Explanation

1. Tokenizer creates a list of tokens by removing chunks from beginning of input.txt until it is empty
2. Token list is iterated over in reverse order, and binary operator tokens are flipped with their following token so as to be after their inputs (converted from infix to postfix)
3. Token list is iterated over in order, and each token has its `eval` method called, with the `stack` passed. The `eval` method may pop items from the stack, do some operation, and push item/s to the stack.

## Examples

### Really janky assignment, recall and addition

```
"foo" = 5 foo log "foo"
log 7 + foo + 2.5 log
```

Assigns `5` to `foo`, logs the value of `foo`, logs the string `foo`, the recalls `foo` and logs `14.5`.

Assignment to a variable is done with a string because reasons

Whitespace/newlines are completely meaningless
