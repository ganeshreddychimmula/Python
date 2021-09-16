from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('H:\sample\\file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



# enter code that reads bytes from the stream here

data1 = bytearray(10)

try:
    bf = open('H:\sample\\file.bin', 'rb')
    bf.readinto(data1)
    bf.close()

    for b in data1:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
