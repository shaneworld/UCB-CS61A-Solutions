class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    (3 4 5)
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '('
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + ')'


def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    s = Link(6, Link(Link(1)))
    s.rest.first.rest = s
    return s


s = strange_loop()
print(s.rest.first.rest is s)


def sum_rec(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_rec(a, 2)
    7
    >>> sum_rec(a, 5)
    15
    >>> sum_rec(Link.empty, 1)
    0
    """
    if k == 0 or s is Link.empty:
        return 0
    if s.rest is Link.empty:
        return s.first
    else:
        return s.first + sum_rec(s.rest, k-1)


print("-------------------------------------------------")
a = Link(1, Link(6, Link(8)))
print(sum_rec(a, 2))
print(sum_rec(a, 5))
print(sum_rec(Link.empty, 1))


def sum_iter(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_iter(a, 2)
    7
    >>> sum_iter(a, 5)
    15
    >>> sum_iter(Link.empty, 1)
    0
    """
    if s is Link.empty:
        return 0
    else:
        return s.first + sum_iter(s.rest, k-1)

print("-------------------------------------------------")
a = Link(1, Link(6, Link(8)))
print(sum_iter(a, 2))
print(sum_iter(a, 5))
print(sum_iter(Link.empty, 1))


def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    if s is Link.empty or t is Link.empty:
        return 0
    if s.first == t.first:
        return 1 + overlap(s.rest, t)
    elif s.first > t.first:
        return 0 + overlap(s, t.rest)
    else:
        return 0 + overlap(s.rest, t)

print("-------------------------------------------------")
a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
print(overlap(a, b))  # 3 and 7
print(overlap(a.rest, b)) # just 7
print(overlap(Link(0, a), Link(0, b)))


def iterate_in_order(s, t):
    """For increasing s and t, yields the elements in s and t, in non-decreasing order.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> t = iterate_in_order(a, b)
    >>> for item in t:
    ...     print(item)
    1
    3
    3
    4
    5
    6
    7
    7
    8
    9
    10
    >>> t = iterate_in_order(Link.empty, b)
    >>> for item in t:
    ...      print(item)
    1
    3
    5
    7
    8
    """
    while s is not Link.empty and t is not Link.empty:
        if s.first > t.first:
            yield t.first
            t = t.rest
        else:
            yield s.rest
            s = s.rest

    while s is not Link.empty:
        yield s.first
        s = s.rest

    while t is not Link.empty:
        yield t.first
        t = t.rest

print("-------------------------------------------------")
a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
t = iterate_in_order(a, b)
