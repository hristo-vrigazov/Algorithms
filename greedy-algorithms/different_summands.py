# Uses python3
import sys

def optimal_summands(n):
    summands = []
    current = n
    magic = 1

    while current is not 0:
    	if current <= 2 * magic:
    		summands.append(current)
    		current -= current
    	else:
    		summands.append(magic)
    		current -= magic
    	magic += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
