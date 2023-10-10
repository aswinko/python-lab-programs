n = int(input("Enter the no of values : "))
list=[]
for i in range(0, n):
    val = int(input("Enter the value : "))
    if val > 100:
        list.append("over")
    else:
        list.append(val)
print(list)