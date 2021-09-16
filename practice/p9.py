#program to acces  envinronmentalvariables
'''An environment variable is a variable whose value is set outside the program, typically through functionality built
into the operating system or microservice.
An environment variable is made up of a name/value pair, and any number may 0+0+550*950+
63be created and available for reference at a point in time.
'''
import os
# Access all environment variables
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')