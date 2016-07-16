from covering_segments import *

assert(optimal_points([\
	Segment(start = 1, end = 3), \
	Segment(start = 2, end = 5), \
	Segment(start = 3, end = 6), \
	]) == [3])

assert(optimal_points([\
	Segment(start = 4, end = 7), \
	Segment(start = 1, end = 3), \
	Segment(start = 2, end = 5), \
	Segment(start = 5, end = 6), \
	]) == [3, 6])