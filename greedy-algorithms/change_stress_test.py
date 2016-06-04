from change import get_change

number_of_ones = 1
number_of_fives = 0
number_of_tens = 0

for i in range(1, 1000):
	expected = number_of_ones + number_of_fives + number_of_tens
	actual = get_change(i)

	print("Input: " + str(i))

	if expected == actual:
		print("OK")
	else:
		print("Fail! Expected " + str(expected) + ", but got " + str(actual) + " instead")

	# if we have for example 9, (5, 1, 1, 1, 1), for 10
	# we get only 10. It also works in other cases
	if i % 10 == 0:
		number_of_tens += 1
		number_of_fives -= 1
		number_of_ones -= 4
		continue

	# if we have for example 4 (1, 1, 1, 1), for 5
	# we get only 5
	if i % 5 == 0:
		number_of_fives += 1
		number_of_ones -= 4
		continue
	number_of_ones += 1
