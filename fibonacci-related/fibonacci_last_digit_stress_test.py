from fibonacci_last_digit import get_fibonacci_last_digit
import math

# We generate test cases, find the
# answer using a naive algorithm
# and then compare it with the more 
# 'intelligent' algorithm
# Note of course that naive algorithm
# has its limitations: its slower, 
# or works on smaller domain

def calc_fib(n):
	phi = (1 + math.sqrt(5)) / 2.0
	return int(round((math.pow(phi, n) - math.pow(-phi, -n)) / math.sqrt(5)))

def naive_fib_last_digit(n):
	return calc_fib(n) % 10

for i in range(70):
	print("Input: " + str(i))

	expected = naive_fib_last_digit(i)
	actual = get_fibonacci_last_digit(i)

	if actual == expected:
		print("OK")
	else:
		print("Expected " + str(expected), ", but got " + str(actual))
		break