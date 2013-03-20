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
dupdir={}       # number of times a dup has been found in a dir -- off by 1

dupSuffix= ".jpg", ".JPG"   # note, must be tuple
for r,d,f in os.walk(dirRoot):
    for files in f:
#            lowerFiles=files.lower() # endswith passed tuple 
#           of files to check.  does this matter? cost of md5sum that high?
            if files.endswith(dupSuffix):
                        fullname= os.path.join(r,files)
                        fileHash = hashlib.md5(open(fullname, 'r').read()).hexdigest()
                        # Check for dup
                        if fileHash in cumulative:  
                            dups.append(fileHash)
                            if dupdir.has_key(r):
                                dupdir[r]+=1
                            else:
                                dupdir[r]=1
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

for k in dupdir:
    print "%s has %s dups in or under it" % (k, dupdir[k])


    
