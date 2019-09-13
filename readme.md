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

1. Doctests

    If you include an interactive python session's output in your functions'
    docstrings, you can use the `doctest` module to test your code.

    Imagine the following code is in `myscript.py`:

    ```python
    def sayhello():
        '''
        Returns a nice, friendly greeting.

        >>> return_value = sayhello()
        >>> return_value
        'Hello, World!'
        '''
    ```

    To test it, run this from your terminal:

    ```
    python -m doctest myscript.py
    ```

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

- Write a function named `chunk`. It should split a list into `n`-sized chunks

    ```python
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> chunk(my_list, 2)
    [[1, 2], [3, 4], [5, 6], [7, 8]]
    >>> chunk(my_list, 3)
    [[1, 2, 3], [4, 5, 6], [7, 8]]
    ```

- Write a function named `map` it should accept a list and a function and apply
  the function to every element in the list

    ```python
    map([1, 2, 3], lambda n: n + 1)
    [2, 3, 4]
    ```

- Write a function named `filter`. It should accept a list and a function and
  return the elements of the list for which the passed function returns true

    ```python
    >>> def is_vowel(c):
    ...    return c in 'aeiou'

    >>> filter(['a', 'b', 'c', 'd', 'e'], is_vowel)
    ['a', 'e']
    ```

- define a `median` function that returns the median of a list of numbers. Be
  sure to handle the case where there are an even number of elements in the
  list.

    ```python
    >>> median([1, 2, 3])
    2
    >>> median([1, 2, 3, 4])
    2.5
    ```

- define a function named `format_phone_number` it should standardize different
  phone number formats

    ```python
    >>> format_phone_number('210.867.5309')
    '(210) 867-5309'
    >>> format_phone_number('2018675309')
    '(210) 867-5309'
    >>> format_phone_number('210-867-5309')
    '(210) 867-5309'
    >>> format_phone_number('(210) 867-5309')
    '(210) 867-5309'
    ```
