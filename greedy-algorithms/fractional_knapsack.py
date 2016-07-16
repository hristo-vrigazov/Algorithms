# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    sorted_by_fraction = sorted(zip(weights, values), key=lambda item: item[1] / item[0])
    value = 0.
    while 0 < capacity and len(sorted_by_fraction):
        weight_i, value_i = c.pop()  # pop the item on top
        x = 1.0
        if weight_i > capacity:
            x = capacity / weight_i
        capacity -= weight_i
        value += x * value_i

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
