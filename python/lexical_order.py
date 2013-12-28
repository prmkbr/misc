#!/usr/local/bin/python

"""
lexical_order.py <n>

Prints the first 'n' numbers in lexicographical order.
"""

import sys

def print_numbers(start, max):
    i = start
    end = ((start + 10) / 10) * 10 - 1 # Next multiple of 10 minus 1
    end = min(end, max)
    while i <= end:
        print i
        print_numbers(i * 10, max)
        i += 1

def main():
    max = int(sys.argv[1]) if len(sys.argv) is 2 else 25
    print_numbers(1, max);

if __name__ == "__main__":
    main()
