# Uses python3
import math

def calc_fib(n):
	phi = (1 + math.sqrt(5)) / 2.0
	return int((math.pow(phi, n) - math.pow(-phi, -n)) / math.sqrt(5))

n = int(input())
print(calc_fib(n))
