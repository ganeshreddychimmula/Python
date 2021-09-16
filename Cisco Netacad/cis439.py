from os import strerror

try:
    bf = open('H:\sample\\file.bin', 'rb')
    data = bytearray(bf.read(7))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# enter code that reads bytes from the stream here