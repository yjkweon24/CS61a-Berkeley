#############
# Iterators #
#############

# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, string):
    	self.string = string
    	self.start = 0
    def __next__(self):
    	self.start += 1
    	if self.start >= len(self.string)+1:
    		raise StopIteration
    	return self.string[self.start -1]
    def __iter__(self):
    	return self

##############
# Generators #
##############

# Q5
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***" 
    for i in s:
    	yield i * k

# Q6
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    i = n 
    while i >= 0:
    	yield i 
    	i -= 1

class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    def __init__(self, cur):
        self.cur = cur

    def __next__(self):
        "*** YOUR CODE HERE ***"
        result = self.cur
        if result < 0:
        	raise StopIteration
        self.cur -= 1
        return result

    def __iter__(self):
        """So that we can use this iterator as an iterable."""
        return self

# Q7
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
    	yield int(n) 
    	if n % 2 == 0:
    		n = n / 2
    	else: 
    		n = n * 3 + 1
    print(1)

# the naturals generator is used for testing scale and merge functions
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1