from fibonacci_huge import get_fibonaccihuge
import math
import random

# We generate test cases, find the
# answer using a naive algorithm
# and then compare it with the more 
# 'intelligent' algorithm
# Note of course that naive algorithm
# has its limitations: its slower, 
# or works on smaller domain

def calc_fib(n):
	phi = (1 + math.sqrt(5)) / 2.0
	return int((math.pow(phi, n) - math.pow(-phi, -n)) / math.sqrt(5))

def naive(n, m):
	return calc_fib(n) % m

for i in range(4, 70):
	k = random.randint(2, i)
	print("Input n = " + str(i) + ", m = " + str(k))
	expected = naive(i, k)
	actual = get_fibonaccihuge(i, k)

	if expected == actual:
		print("OK")
	else:
		print("Expected " + str(expected) + " but got " + str(actual) + " instead")
		break