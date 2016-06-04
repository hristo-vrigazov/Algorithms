# Uses python3
import sys

def get_change(n):

	number_of_tens = n // 10
	number_of_fives = (n % 10) // 5
	number_of_ones = n % 5

	return number_of_ones + number_of_fives + number_of_tens

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
