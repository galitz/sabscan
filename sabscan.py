#!/usr/bin/python

import sys


# take address range from command line, last octent only


start = int(sys.argv[1])
end = int(sys.argv[2])

print ("Start = " + str(start) + " End = " + str(end))

while True:
        print " ", start
        start += 1
        if start == end:
                break
	# function to to scan goes here
print "done"

