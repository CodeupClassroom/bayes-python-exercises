def remove_special_chars(s):
    return ''.join([c for c in s if c.isidentifier() or c == ' '])
 
def normalize_name(s):
    return remove_special_chars(s).lower().strip().replace(' ', '_')

def cumsum(xs):
    sums = [xs[0]]
    for x in xs[1:]:
        sums.append(sums[-1] + x)
    return sums

def lookup_letter(c):
    return 'abcdefghijklmnopqrstuvwxyz'.index(c) + 1









def lookup_letter(c):
    return 'abcdefghijklmnopqrstuvwxyz'.index(c.lower()) + 1
def lookup_column(s):
    return sum([lookup_letter(c) * 26 ** i for i, c in enumerate(s)])
