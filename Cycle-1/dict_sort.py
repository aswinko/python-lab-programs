fruits = {'apple': 2, 'orange': 14, 'pineapple': 31, 'watermelon': 61, 'grapes': 10}
item = list(fruits.items())
item.sort()
print("Ascending order : ", item)

item.sort(reverse=True)
print("Descending order : ", item)