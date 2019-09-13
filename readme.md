# Bayes Python Exercises

This repository contains instructor-provided lecture notes, exercise solutions,
and additional materials for the python module.

## How do I know if my code is correct?

1. `assert` or `print` within your script

    ```python
    def sayhello():
        return 'hello, world!'

    assert sayhello() == 'hello, world', "sayhello() should return 'hello, world!'"
    ```

    ```python
    def sayhello():
        return 'hello, world!'

    print('return value of sayhello() below:')
    print(sayhello())
    ```

1. Test the code in your script interactively

    From your terminal:

    ```
    ipython -i myscript.py
    ```

    Replacing `myscript.py` with the name of your python file.

## Function Bonuses

if you've finished all the bonuses in the curriculum...

- define the following functions

    - `add(x, y)`
    - `subtract(x, y)`
    - `multiply(x, y)`
    - `divide(x, y)`

    - **bonus**: define multiply without using the `*` operator
    - **bonus**: define divide without using the `/` operator
    - **bonus bonus**: define multiply without using a loop or the `*` operator
    - **bonus bonus**: define divide without using a loop or the `/` operator
