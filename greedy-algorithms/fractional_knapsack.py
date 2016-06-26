# Uses python3
import sys

# def get_optimal_value(capacity, weights, values):
#     value = 0.

#     def bag_is_not_full():
#     	return capacity > 0

#     def there_are_items_left():
#     	return len(weights) != 0
#    	# print(weights)
#    	# print(values)
#     while bag_is_not_full() and there_are_items_left():
#     	def find_best_value_weight_ratio(weights, values):
#     		best_index = 0
#     		best_ratio = weights[0] / float(values[0])
#     		for i in range(len(weights)):
#     			cache = weights[i] / float(values[i])
#     			if cache < best_ratio:
#     				best_index = i
#     				best_ratio = cache
#     		return best_index

#     	best_value_weight_ratio_index = find_best_value_weight_ratio(weights, values)

#     	if weights[best_value_weight_ratio_index] >= capacity:
#     		value += (capacity / float(weights[best_value_weight_ratio_index])) * values[best_value_weight_ratio_index]
#     		capacity = 0
#     	else:
#     		value += values[best_value_weight_ratio_index]
#     		capacity -= weights[best_value_weight_ratio_index]
#     	del weights[best_value_weight_ratio_index]
#     	del values[best_value_weight_ratio_index]

#     return value

def get_optimal_value(capacity, weights, values):
    c = sorted(zip(weights, values), key=lambda item: item[1] / item[0])
    value = 0.
    while 0 < capacity and len(c):
        wi, vi = c.pop()  # get item with highest (value / weight) value
        xi = 1.0
        if wi > capacity:
            xi = capacity / wi
        capacity -= wi
        value += xi * vi

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
