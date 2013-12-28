#!/usr/local/bin/python

"""
Prints the numbers from 1 to 100. But for multiples of three print 'Fizz'
instead of the number and for the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print 'FizzBuzz'.
"""

def main():
    """
    Main body of the script.
    """
    for i in xrange(1, 101):
        if i % 5 == 0:
            print "FizzBuzz" if (i % 3 == 0) else "Buzz"
        elif i % 3 == 0:
            print "Fizz"
        else:
            print i

if __name__ == "__main__":
    main()
