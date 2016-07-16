# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # sort the points by their right point
    segments.sort(key=lambda x: x.end)
    # add the right point of the most left segment
    points = [segments.pop(0).end]
    # now we will add only right points of segments
    for s in segments:
        # if the left point in the current segment
        # is more to the right than the last added
        # right point, then append the right end
        # of the segment
        if s.start > points[-1]:
            points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
