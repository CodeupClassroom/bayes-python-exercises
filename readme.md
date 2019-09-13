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

- define a function named `roll_dice` it will accept a specially formatted input
  string and return a list of the random dice rolls specified

    The input string will look like one of the following:

    - `1d6` means roll 1 6-sided die
    - `3d6` means roll 3 6-sided dice
    - `4d4` means roll 4 4-sided dice

    The code below will produce a random number between 1 and 6:

    ```python
    from random import randint

    random_number = randint(1, 6)
    ```

    Examples:

    ```python
    >>> roll_dice('4d4')
    [1, 3, 2, 2]
    >>> roll_dice('2d10')
    [8, 3]
    ```

    **Bonus**

    Instead of a list, have your function return a dictionary that contains bits
    of information about the rolls

    Examples:

    ```python
    >>> roll_dice('4d4')
    {"mean": 2.0, "sum": 8, "rolls": [1, 3, 2, 2]}
    >>> roll_dice('2d10')
    {"mean": 5.5, "sum": 11, "rolls": [8, 3]}
    ```
