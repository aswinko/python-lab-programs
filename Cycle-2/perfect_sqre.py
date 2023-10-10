lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))

sqr = [i for i in range(lower, upper+1) if((i**0.5) == int(i**0.5)) and i % 2 == 0]
print(sqr)
