from gcd import gcd
import math
import random

# We generate test cases, find the
# answer using a naive algorithm
# and then compare it with the more 
# 'intelligent' algorithm
# Note of course that naive algorithm
# has its limitations: its slower, 
# or works on smaller domain

def is_prime(n):
	if n < 2:
		return False

	for i in range(2, n - 1):
		if n % i == 0:
			return False

	return True

def primes_less_than(n):
	primes = list()
	for i in range(n):
		if is_prime(i):
			primes.append(i)
	return primes

for i in range(2, 40):
	feasible_primes = primes_less_than(i)
	if len(feasible_primes) >= 2:
		random_two = random.sample(feasible_primes, 2)
		a = random_two[0] * i
		b = random_two[1] * i
		print("Input: a = " + str(a) + ", b = " + str(b))
		expected = i
		actual = gcd(a, b)

		if expected == actual:
			print("OK")
		else:
			print("Expected " + str(expected) + " but got " + str(actual) + " instead")
			break

