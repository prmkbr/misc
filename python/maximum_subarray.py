#!/usr/bin/env python

"""
maximum_subarray.py

Prints the largest sum of a subarray within an array of numbers.

http://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

import numpy as np

def maximum_subarray(arr):
    overall_max = cur_max = 0
    max_start = max_end = cur_start = cur_end = None
    for i in xrange(len(arr)):
        n = arr[i]
        if (cur_max + n > 0):
            cur_max += n
            cur_start = i if cur_start is None else cur_start
            cur_end = i
        else:
            cur_max = 0
            cur_start = cur_end = None

        if (cur_max > overall_max):
            overall_max = cur_max
            max_start = cur_start
            max_end = cur_end

    return (max_start, max_end, overall_max)

def main():
    na = np.random.randint(low=-20, high=20, size=10)
    print "Array:", na
    res = maximum_subarray(na)
    print "Maximum subarray: ", res[:2], " sum: ", res[-1]

if __name__ == "__main__":
    main()
