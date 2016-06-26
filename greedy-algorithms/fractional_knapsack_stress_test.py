from fractional_knapsack import get_optimal_value

# print get_optimal_value(capacity=50, weights=[20, 50, 30], values=[60, 100, 120])
# print get_optimal_value(capacity=10, weights=[30], values=[500])
print get_optimal_value(capacity=28, weights=[30], values=[500])

# assert get_optimal_value(capacity=50, weights=[20, 50, 30], values=[60, 100, 120]) == 180
# assert get_optimal_value(capacity=10, weights=[30], values=[100]) == 166.667