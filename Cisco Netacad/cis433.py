#stream=open("H:\html\hi.txt",'rt',)
#import sys
#stream.close()
#hi=sys.stdin
#ri=sys.stderr
#import errno
#for i in dir(errno):
 #   print(i)
import errno
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # actual processing goes here
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        printf("The error number is:", exc.errno)

from os import strerror
try:
    s = open("H:\html\hi.txt", "rt")
    # actual processing goes here
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno));