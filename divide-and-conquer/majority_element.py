# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    half = (right - left) // 2
    majority_left = get_majority_element(a, left, left + half)
    majority_right = get_majority_element(a, left + half, right)

    majority_left_counter = 0
    majority_right_counter = 0

    for v in a[left:right]:
        if v == majority_left:
            majority_left_counter += 1
        if v == majority_right:
            majority_right_counter += 1

    if majority_left_counter > half:
        return majority_left
    if majority_right_counter > half:
        return majority_right

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
