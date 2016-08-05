#Uses python3
#Ugliest code I have ever written

import sys

def bigger_than(X, Y):
	return (X + Y) > (Y + X)

def find_biggest_index(a):
	max_index = 0
	for i in range(len(a)):
		if bigger_than(a[i], a[max_index]):
			max_index = i
	return max_index

def largest_number(a):
	answer = ""

	while a:
		biggest_index = find_biggest_index(a)
		answer += a[biggest_index]
		del(a[biggest_index])

	return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
