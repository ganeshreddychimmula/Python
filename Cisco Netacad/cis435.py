from os import strerror

try:
    cnt = 0
    s = open('H:\sample\sample.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))