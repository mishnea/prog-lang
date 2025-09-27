# Prog Lang Examples

## Notes

- `$` creates a placeholder and allows variables to take new values
- `->` pipe takes all values on the left and passes them to the expression on the right

## Examples

### Print the first two arguments to console. store remaining args in an array

Starting with pipe forwards the arguments passed to the program

```
-> log($[2]), $args[];
```

### Pop first two elements of `args` array into `x` and `y`. Add them, and store the result in `z`

This redefines `args` as an array containing just the remaining arguments, making it effectively the same as popping

```
args -> $x + $y, $args[] -> $z;
```

### Use a block. Variables initialised within a block are locally scoped

```
1, 2 -> $x, $y;
x -> {
    $ + 3 -> $x
} -> $y;
log(x); // 1
log(y); // 4
```

### Declare a function, `some_function`

```
// Function parameters are placeholders/variable holders
fn some_function( $x, $ ) -> {
    // Define y, then log the first argument
    $, $y -> log($);
    // Return sum of `x` and `y`
    return x + y;
}
```

### Create a function which finds the length of an array

```
// Store input into an array of any length
fn len( $arr[] ) {
    // Initialise `i` to an integer of 0
    0 -> $i;
    // While an element of `arr` can be popped into `x`
    while (arr -> $x, $arr[]; x != null) {
        // Log the value of `x`
        log(x);
        // Increment `i`
        i + 1 -> $i;
    }
    // Return the final value of `i`
    return i;
};
```

### Conditionals

```
-> if ($ == "hello") {
    log("hello world!")
} else {
    log("unknown argument", $)
}
