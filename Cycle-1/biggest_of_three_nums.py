num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))

if (num1 > num2) and (num1 > num3):
    print(num1, " is Biggest.")
elif (num2 > num3) and (num2 > num1):
    print(num2, " is Biggest.")
else:
    print(num3, " is Biggest.")
