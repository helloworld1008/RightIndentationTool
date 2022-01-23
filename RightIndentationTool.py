#!/usr/bin/env python

import os,subprocess
from datetime import datetime

print ""

filename = raw_input("Enter absolute path of file: ")	# Eg. /tmp/myfile

print ""

new_file_name = filename.split("/")[-1] + "_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".orig"	# Eg. myfile_22_01_2022_12_27_43.orig

new_file_path = "/".join(filename.split("/")[0:-1]) + "/" + new_file_name	# Eg. /tmp/myfile/myfile_22_01_2022_12_27_43.orig

fo = open(new_file_path, "w")

for line in open(filename, "r"):

	fo.write(line)

fo.close()

print "Original file saved to {}".format(new_file_path)
print ""

linecount = 1

for line in open(filename,'r'):

	print linecount,line,

	linecount = linecount + 1

print ""

start_line_number = raw_input("Enter start line number: ")
print ""
end_line_number = raw_input("Enter end line number: ")
print ""


subprocess.call(["rm",filename])

fo = open(filename,"w")

linecount = 1

for line in open(new_file_path,'r'):

	if linecount >= int(start_line_number) and linecount <= int(end_line_number):

		fo.write("\t" + line)
		#print "\t" + line,

	else:

		fo.write(line)
		#print line,

        linecount = linecount + 1

fo.close()

print "File {} modified".format(filename)

print ""
