a = input("Enter the string 1 : ")
b = input("Enter the string 2 : ")

#print(a.replace(a[0], b[0]), b.replace(b[0], a[0]))

print(b[0]+a[1:] + " " + a[0]+b[1:])