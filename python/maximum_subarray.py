#!/usr/bin/env python

"""
maximum_subarray.py

Prints the largest sum of a subarray within an array of numbers.

http://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

import numpy as np

def maximum_subarray(arr):
    overall_max = cur_max = 0
    for n in arr:
        cur_max = max(0, cur_max + n)
        overall_max = max(overall_max, cur_max)
    return overall_max

def main():
    na = np.random.randint(low=-20, high=20, size=10)
    print "Array:", na
    print "Maximum subarray sum:", maximum_subarray(na)

if __name__ == "__main__":
    main()
