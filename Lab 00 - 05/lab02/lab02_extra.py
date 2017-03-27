"""Optional program for lab02 """

from lab02 import *

# Recursion

def factorial(n):
	"""Return n * (n - 1) * (n - 2) * ... * 1.

	>>> factorial(5)
	120
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def skip_mul(n):
	"""Return the product of n * (n - 2) * (n - 4) * ...

	>>> skip_mul(5) # 5 * 3 * 1
	15
	>>> skip_mul(8) # 8 * 6 * 4 * 2
	384
	"""
	if n == 2:
		return 2
	elif n ==1:
		return 1
	else:
		return n * skip_mul(n - 2)

def gcd(a, b):
	"""Returns the greatest common divisor of a and b.
	Should be implemented using recursion.

	>>> gcd(34, 19)
	1
	>>> gcd(39, 91)
	13
	>>> gcd(20, 30)
	10
	>>> gcd(40, 40)
	40
	"""
	"*** YOUR CODE HERE ***"
	x = min (a, b)
	def helper(a, b, dividend, gcdsaver):
		if (dividend > x):
			return gcdsaver
		elif (a % dividend != 0) or (b % dividend !=0):
			return helper(a, b, dividend+1, gcdsaver)
		elif (a % dividend == 0) and (b % dividend ==0):
			gcdsaver = dividend
			return helper(a, b, dividend+1, gcdsaver)
	return helper(a, b, dividend = 1, gcdsaver =1)

print(gcd(40, 40))


# Higher Order Functions

def count_cond(condition):
	"""Returns a function with one parameter N that counts all the numbers from
	1 to N that satisfy the two-argument predicate function CONDITION.

	>>> count_factors = count_cond(lambda n, i: n % i == 0)
	>>> count_factors(2)   # 1, 2
	2
	>>> count_factors(4)   # 1, 2, 4
	3
	>>> count_factors(12)  # 1, 2, 3, 4, 6, 12
	6

	>>> is_prime = lambda n, i: count_factors(i) == 2
	>>> count_primes = count_cond(is_prime)
	>>> count_primes(2)    # 2
	1
	>>> count_primes(3)    # 2, 3
	2
	>>> count_primes(4)    # 2, 3
	2
	>>> count_primes(5)    # 2, 3, 5
	3
	>>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
	8
	"""
	"*** YOUR CODE HERE ***"
	def counter(n):
		i, count = 1, 0
		while i <= n:
			if condition(n, i):
				count += 1
			i += 1
		return count
	return counter

def cycle(f1, f2, f3):
	"""Returns a function that is itself a higher-order function.

	>>> def add1(x):
	...     return x + 1
	>>> def times2(x):
	...     return x * 2
	>>> def add3(x):
	...     return x + 3
	>>> my_cycle = cycle(add1, times2, add3)
	>>> identity = my_cycle(0)
	>>> identity(5)
	5
	>>> add_one_then_double = my_cycle(2)
	>>> add_one_then_double(1)
	4
	>>> do_all_functions = my_cycle(3)
	>>> do_all_functions(2)
	9
	>>> do_more_than_a_cycle = my_cycle(4)
	>>> do_more_than_a_cycle(2)
	10
	>>> do_two_cycles = my_cycle(6)
	>>> do_two_cycles(1)
	19
	"""
	"*** YOUR CODE HERE ***"
	def helper(n):
		def ret(x):
			i = 1
			while i <= n:
				if i % 3 == 1:
					x = f1(x)
					i += 1
				elif i % 3 == 2:
					x = f2(x)
					i += 1
				else:
					x = f3(x)
					i += 1 
			return x
		return ret
	return helper
