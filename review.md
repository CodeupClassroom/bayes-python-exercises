# Python Review

## Data Types, Operators, and Variables

- Fundamental Data Types
    - bool
    - str
    - int and float
    - list
    - dict
    - None
- Operators are *overloaded*, meaning they do different things depending on the
  context
    - not all operators can be used with all data types
    - arithmatic operators
    - comparison operators
- string methods + formatting
- manipulating existing lists + list comprehensions
- tuples
- dictionaries
    - reading dictionary values
    - modifying existing dictionary values
    - creating new dictionary values

## Control Structures

- conditionals: execute code conditionally (i.e. based on a boolean value)
    - `if`
    - `if` - `else`
    - `if` - `elif` - `else`
- loops: execute code repeatedly
    - `while`: execute until a condition is met
    - `for`: iterate over a list of things, do something for every element; much
      more common than `while`
    - `break`: exit the loop
    - `continue`: skip to the next loop cycle

## Functions

- built in functions
- calling functions
- control flow wrt functions
- defining functions
    - parameters
    - return
    - arguments
- local vs global scope
- *args & kwargs
- lambda functions

## Imports

- `import`, `as`, `from`

## Assessment-Style Problems

1. Write a function named `keep_long_words`. It should accept a list of strings
   and return a list of the strings that are more than 4 characters long.

    ```python
    >>> keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])
    ['codeup', 'bayes']
    >>> keep_long_words(['cd', 'ls', 'pwd'])
    []
    >>> keep_long_words(['python', 'algorithm'])
    ['python', 'algorithm']
    ```

1. Write a function named `make_model`. It will accept a list of dictionaries
   where each dictionary represents a car, and return a list of strings where
   each string is the make and model of the car concatenated together.

    ```python
    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']
    ```

1. Write a function named `extract_time_components`. It should take in a string
   that is a 24-hour time with the hour, minutes, and seconds seperated by `:`s,
   and return a dictionary with keys `hour`, `minutes`, and `seconds` with
   corresponding integer values.

    ```python
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    ```
