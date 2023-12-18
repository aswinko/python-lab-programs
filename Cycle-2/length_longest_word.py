list = ["Hello", "Word", "Programming"]
print(list)
a=0
for i in list:
    a=len(i) if len(i) > a else a
print("Length of longest word is  : ", a)