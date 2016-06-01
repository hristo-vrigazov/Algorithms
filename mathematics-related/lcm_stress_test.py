from lcm import lcm
from lcm import gcd
import random

# We generate test cases, find the
# answer using a naive algorithm
# and then compare it with the more 
# 'intelligent' algorithm
# Note of course that naive algorithm
# has its limitations: its slower, 
# or works on smaller domain

while True:
	a = random.randint(4, 100)
	b = random.randint(4, 100)

	print("Input a = " + str(a) + ", b = " + str(b))

	gcd_a_b = gcd(a, b)

	expected = (a * b) / gcd_a_b
	actual = lcm(a, b)

	if expected == actual:
		print("OK")
	else:
		print("Expected " + str(expected) + ", but got " + str(actual) + " instead")