# To find positive numbers from list
list = [-1, 3, 3, 76, -4, -23, 54]
print("Positive number are : ")
p = [i for i in list if i >= 0]
print(p)

# To find square of list
list2 = [1, 2, 3, 4, 5, 6, 34, 78, 4, 8]
print("List ", list2)
print("Square of list 2 : ")
t = [(x ** 2) for x in list2]
print(t)

# Check vowel or not
vowel = ['a', 'e', 'i', 'o', 'u']
w = input("Enter a word :  ")
w = w.lower()
s = [i for i in w if i in vowel]
print(s)

# List Ordinal value
word = input("Enter the word ")
j = [ord(x) for x in word]
print(j)

