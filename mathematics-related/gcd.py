# Uses python3
import sys

def gcd(a, b):
	q = a
	r = b
	
	while q % r != 0:
		old_q = q
		q = r
		r = old_q % r
		
	return r

if __name__ == "__main__":
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(gcd(a, b))
