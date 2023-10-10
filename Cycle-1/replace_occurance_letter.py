string = input("Enter the string : ")
firstChar = string[0]
string = string.replace(firstChar, "$")
print(firstChar + string[1:])