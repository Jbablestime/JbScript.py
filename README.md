# Jb Script
Jb Script is a custom coding language coded in Python, it makes Python easier to code by rewriting basic syntax.

## Code Example
```
variable(name="var_1", value="This is the var_1 value")
wait(5)
send(var_1)
```

## Run Code
- CD to the directory holding the Jb Script folder.
- Run `python main.py script.jb`
- Run silent `python main.py script.jb -s`

## Syntax
- `send("message-here")` - Prints text to console.
- `variable(name="variable-name", value="variable-value")` - Stores a value by name, can be used in `send()`.
- `wait(number-here)` - Waits the entered amount in seconds.
