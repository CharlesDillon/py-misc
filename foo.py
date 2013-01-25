#! /usr/bin/python

# infile= open('sum.txt', 'r')
x = 0
fsum ={}
flen ={}
for line in open('sum.txt', 'r').readlines():
	l = line.split()
	print x, l[0], l[1], l[2]
	fsum[l[2]]=l[0]
	flen[l[2]]=l[1]
	x=x+1
	
