class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        self.a = self.l * self.b
        return self.a
    def display(self):
        print("Area of rectangle : ", self.a)
    def __lt__(self, obj):  
        if (self.area() < obj.area()):
            return "The area of rectangle 1 is less than rectangle 2."
        else:
            return "The area of rectangle 2 is less tha rectangle 1."

print("Rectangle 1")
len1 = int(input("Enter the Length 1 : "))
bred1 = int(input("Enter the Breadth 1 : "))

print("Rectangle 2")
len2 = int(input("Enter the Length 2 : "))
bred2 = int(input("Enter the Breadth 2 : "))

obj1 = Rect(len1, bred1)
obj2 = Rect(len2, bred2)

obj1.area()
obj2.area()

print(obj1 < obj2)