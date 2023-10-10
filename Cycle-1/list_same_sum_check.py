list1 = [2, 5, 7, 32, 8]
list2 = [3, 43, 32, 98, 4]

print(list1)
print(list2)

print("Length of list 1 : ", len(list1))
print("Length of list 2 : ", len(list2))
if len(list1) == len(list2):
    print("Length of list are same.")
else:
    print("Length of list are not same.")

print("Sum list 1 : ", sum(list1))
print("Sum of list 2 : ", sum(list2))
if sum(list1) == sum(list2):
    print("Sum of two list are same.")
else:
    print("Sum of list are not same")

check = any(item in list1 for item in list2)
print("Any value occur in both :", check)