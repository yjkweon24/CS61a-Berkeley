def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    x = min(a, b)
    result = max(a, b)
    product = a * b
    while (result <= product):
        if (result % a == 0):
            if (result % b == 0):
                return result
        result += 1

    return result

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    while (n != 0):
        digitnumber = n % 10
        list[digitnumber] = 0
        n = n // 10

    count = 0
    i = 0
    for i in range(10):
        if (list[i] == 0):
            count += 1
            i += 1
        else:
            i +=1
    return count
