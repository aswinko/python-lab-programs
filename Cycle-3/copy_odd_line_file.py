file1 = open("sample.txt", "r")
file2 = open("demo.txt", "w")

fl = file1.readlines()
for i in range(0, len(fl)):
    if i % 2 == 0:
        file2.write(fl[i])
    else:
        pass
file2.close()
file2 = open("demo.txt", "r")
e = file2.read()
print(e)
file1.close()
file2.close()