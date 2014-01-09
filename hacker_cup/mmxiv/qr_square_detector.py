#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        N = int(sys.stdin.readline())

        min_x, min_y = N, N
        max_x, max_y = -1, -1
        total_hash = 0

        for j in xrange(N):
            line = sys.stdin.readline()
            line_hash = line.count('#')
            if line_hash > 0:
                total_hash += line_hash
                min_x = min(min_x, line.find('#'))
                max_x = max(max_x, line.rfind('#'))
                min_y = min(min_y, j)
                max_y = max(max_y, j)

        squared = (max_x - min_x == max_y - min_y) and  \
                  (total_hash == 0 or total_hash == (max_x - min_x + 1) ** 2)
        print "Case #%d: %s" % ((i+1), "YES" if squared else "NO")

if __name__ == "__main__":
    main()
