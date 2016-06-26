from binary_search import binary_search
import random

def generate_input():
	array = []
	temp = 10
	number_to_search = -1
	for i in range(random.randint(0, 10)):
		temp = random.randint(temp, temp + random.randint(5, 60))
		if random.randint(0, 4) == 0:
			number_to_search = temp
		array.append(temp)

	if random.randint(0, 4) == 0:
		number_to_search = -1
	return array, number_to_search

def linear_search(array, number):
	for i in range(len(array)):
		if array[i] == number:
			return i
	return -1

while True:
	array, number = generate_input()
	expected = linear_search(array, number)
	actual = binary_search(array, number)

	print("Array " + str(array))
	print("Number " + str(number))

	if expected != actual:
		print("Wrong!")
		print("Expected :" + str(expected))
		print("Actual: " + str(actual))
		break
	else:
		print("OK")