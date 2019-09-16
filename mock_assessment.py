def remove_special_chars(s):
    return ''.join([c for c in s if c.isidentifier() or c == ' '])

def normalize_name(s):
    return remove_special_chars(s).lower().strip().replace(' ', '_')

def cumsum(xs):
    sums = [xs[0]]
    for x in xs[1:]:
        sums.append(sums[-1] + x)
    return sums

# Bonuses

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

# # without `*`
# def multiply(x, y):
#     '''
#     >>> multiply(2, 3)
#     6
#     >>> multiply(5, 8)
#     40
#     '''
#     result = 0
#     for _ in range(y):
#         result += x
#     return result

# without `*` or a loop, using recursion
def multiply(x, y):
    '''
    >>> multiply(2, 3)
    6
    >>> multiply(5, 8)
    40
    '''
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    return x + multiply(x, y - 1)

# recursive, doesn't handle remainders
def divide(x, y):
    '''
    >>> divide(8, 2)
    4
    >>> divide(12, 3)
    4
    '''
    if x == 0 or y == 0:
        return 0 # technically y = 0 causes a divide by 0 error
    if y >= x:
        return 1
    return 1 + divide(x - y, y)

from random import randint
# v1
def roll_dice(s):
    n_dice, n_sides = [int(n) for n in s.split('d')]
    return [randint(1, n_sides) for _ in range(n_dice)]
# v2
def roll_dice(s):
    n_dice, n_sides = [int(n) for n in s.split('d')]
    rolls = [randint(1, n_sides) for _ in range(n_dice)]
    return {'rolls': rolls, 'sum': sum(rolls), 'mean': sum(rolls) / len(rolls)}

def chunk(xs, n):
    '''
    >>> my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> chunk(my_list, 2)
    [[1, 2], [3, 4], [5, 6], [7, 8]]
    >>> chunk(my_list, 3)
    [[1, 2, 3], [4, 5, 6], [7, 8]]
    '''
    return [xs[i:i + n] for i in range(0, len(xs), n)]

def map(xs, f):
    '''
    >>> map([1, 2, 3, 4], lambda n: n + 1)
    [2, 3, 4, 5]
    '''
    return [f(x) for x in xs]

def filter(xs, f):
    '''
    >>> def is_vowel(c):
    ...    return c in 'aeiou'
    >>> filter(['a', 'b', 'c', 'd', 'e'], is_vowel)
    ['a', 'e']
    '''
    return [x for x in xs if f(x)]

def median(xs):
    '''
    >>> median([1, 2, 3])
    2
    >>> median([1, 2, 3, 4])
    2.5
    >>> median([1, 2, 3, 4, 5, 6])
    3.5
    >>> median([1, 2, 3, 4, 5, 6, 7])
    4
    '''
    midpoint = len(xs) // 2
    length_is_even = len(xs) % 2 == 0
    if length_is_even:
        return (xs[midpoint - 1] + xs[midpoint]) / 2
    else:
        return xs[midpoint]

def format_phone_number(s):
    '''
    >>> format_phone_number('210.867.5309')
    '(210) 867-5309'
    >>> format_phone_number('2108675309')
    '(210) 867-5309'
    >>> format_phone_number('210-867-5309')
    '(210) 867-5309'
    >>> format_phone_number('(210) 867-5309')
    '(210) 867-5309'
    '''
    digits = ''.join([c for c in s if c in '0123456789'])
    return '({}) {}-{}'.format(digits[:3], digits[3:6], digits[6:])

def lookup_letter(c):
    return 'abcdefghijklmnopqrstuvwxyz'.index(c.lower()) + 1

def lookup_column(s):
    '''
    >>> lookup_column('A')
    1
    >>> lookup_column('B')
    2
    >>> lookup_column('AA')
    27
    '''
    return sum([lookup_letter(c) * 26 ** i for i, c in enumerate(s)])
