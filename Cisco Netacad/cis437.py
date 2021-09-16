from os import strerror

try:
	f = open('H:\sample\\newtext.txt', 'wt') # a new file (newtext.txt) is created
	for i in range(10):
			f.write("line #" + str(i+1) + "\n")
	f.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
import sys
#sys.stderr.write("error messsage")