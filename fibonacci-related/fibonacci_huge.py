# Uses python3
import sys

import math

# returns Fn mod m for big n
# for more information, see problem 5 in the pdf
# The remainders are actually periodic
# See Pisano period - the period always
# starts with 01, so we simply go until
# we find it

def get_fibonaccihuge(n, m):
	fibPrev = 0
	fib = 1
	cached = [fibPrev, fib]

	for curr in range(1, n):
		fibOld = fib
		fib = (fib + fibPrev) % m
		fibPrev = fibOld
		if fibPrev == 0 and fib == 1:
			cached.pop()
			break
		else:
			cached.append(fib)

	offset = n % len(cached)
	return cached[offset]

if __name__ == '__main__':
	input = sys.stdin.read();
	n, m = map(int, input.split())
	print(get_fibonaccihuge(n, m))
