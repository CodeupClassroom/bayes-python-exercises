# Custom Sorting in Python

Let's suppose we have a list of dictionaries, where each dictionary
represents a person.

```python
people = [{
    'name': 'Peter',
    'pieces_of_flair': 5
}, {
    'name': 'Joanna',
    'pieces_of_flair': 14
}, {
    'name': 'Samir',
    'pieces_of_flair': 4
}, {
    'name': 'Milton',
    'pieces_of_flair': 9
}]
```

What if we wanted to sort our list? Simply calling `sorted` will fail,
because python doesn't know how to compare two dictionaries.

```python
sorted(people)
```

To illustrate:

```python
{} < {}
```

The same will hold true for the `min` and `max` functions, for the same
reason (python doesn't know how to compare dictionaries).

We can, however, supply a keyword argument, `key` to tell python how to do
the sorting. The function we supply should accept a single element of the
list and return a value that can be sorted. For example, we could sort the
list of people alphebetically by name by telling python to access the value
corresponding to the `name` key for each list element:

```python
sorted(people, key=lambda person: person['name'])
```

Or we could sort numerically by peices of flair by specifying that key:

```python
sorted(people, key=lambda person: person['pieces_of_flair'])
```

We can use this functionality to specify a custom sorting behavior by mapping
our existing list elements to a value that pyhon knows how to sort. We could
even use this to override the default sorting behavior.

For example, imagine we have a list of strings and want to sort the list by
string length.

```python
strings = ['betelgeuce', 'aardvark', 'bayes', 'ciao']
```

By default, python will sort the list alphebetically:

```python
sorted(strings)
```

But we can sort the list by string length by supplying a function that maps
each string to it's length.

```python
sorted(strings, key=lambda s: len(s))
```

