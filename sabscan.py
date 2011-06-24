#!/usr/bin/python

import sys, ping


# take address range from command line, last octent only

command = sys.argv[1]
net = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])


if command == "scannet":
	addr = net
	print "Network scan of " + net + " network"
	print ("Start = " + str(start) + " End = " + str(end))

while True:
        print " ", start
        start += 1
        if start == end:
                break
	# function to to scan goes here
	target = addr + start
	# scantarget
print "done"

