#! /usr/bin/env python2.7

import sys
import os
import hashlib

# TODO replace the default and argparse the params
# import argparse
# TODO multiple roots / directory trees to search

defaultRoot = "/media/mirror/share"
jpegcount = 0

if len(sys.argv) < 2:
    print "using default root %s" % defaultRoot
    dirRoot = defaultRoot 
else:
    dirRoot = sys.argv[1]

# script_name, one = sys.argv
# keep list of md5sums
# keep dictionary of fullnames and associated md5sums
# keep list of collisions/duplicates
dups=[]         # list of duplicates
cumulative=[]   # all the md5sums -- check dups first
fileList={}     # all files with associated md5 {full path: sum}
dupdir={}

for r,d,f in os.walk(dirRoot):
    for files in f:
            lowerFiles=files.lower()
            if lowerFiles.endswith(".jpg"):
                        fullname= os.path.join(r,files)
                        fileHash = hashlib.md5(open(fullname, 'r').read()).hexdigest()
                        if fileHash in cumulative:
                            dups.append(fileHash)
                            if dupdir.has_key(files):
                                dupdir[files]+=1
                            else:
                                dupdir[files]=1
#                            print "dup"     # which clearly isnt true
                        cumulative.append(fileHash)
                        fileList[fullname]=fileHash
#                        print "r is %s  d is %s   f is %s" % (r,d,f)
                    
                        jpegcount += 1
print "number of pictures", jpegcount
print "number of dupes", len(dups), ":"

for j in dups:
    print "for md5sum ",j
    for i in fileList.iterkeys():
        if fileList[i] == j:
            print i
    print " "


    
