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

def lcm(a, b):
    #write your code here
    return int(int((a*b)) // int(gcd(a, b)))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

