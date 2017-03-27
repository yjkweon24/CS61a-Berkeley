from utils import *

# Q1
from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    dis = sqrt(((get_lat(city1)) - get_lat(city2))**2 + ((get_lon(city1)) - get_lon(city2))**2)
    return dis

# Q2
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    dis1 = sqrt(((get_lat(city1)) - lat)**2 + ((get_lon(city1)) - lon)**2)
    dis2 = sqrt(((get_lat(city2)) - lat)**2 + ((get_lon(city2)) - lon)**2)
    if dis1 > dis2:
        return get_name(city2)
    else:
        return get_name(city1)
    '''
    center = make_city("centercity", lat, lon)
    dis1 = distance(center, city1)
    dis2 = distance(center, city2)
    -> and compare
    '''
# Q3
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    if (a == 0):
        return c
    else:
        return ab_plus_c(a-1, b, c) + b

# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    def help(n, i):
        if (i == 1):
            return True
        if (n%i == 0):
            return False
        return help(n, i-1)

    return help(n, n-1)
