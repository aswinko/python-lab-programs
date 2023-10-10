for i in range(int(input("Enter the initial year : ")), int(input("Enter the final year : "))):
    if (i % 4 == 0) and (i % 100 != 0):
        print(i)
