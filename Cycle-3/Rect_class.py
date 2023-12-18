class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        self.a = self.l * self.b
    def per(self):
        self.p = 2 * self.l + self.b
    def compare(self, obj):
        if self.a == obj.a:
            print("Both areas are same.")
        elif self.a > obj.a:
            print("Area 1 is greater than Area 2.")
        else:
            print("Area 2 is greater than Area 1")
    def display(self):
        print("Area of rectangle = ", self.a)
        print("Perimeter of rectangle = ", self.p)


len1 = int(input("Enter the Length 1 : "))
bred1 = int(input("Enter the Breadth 1 : "))

len2 = int(input("Enter the Length 2 : "))
bred2 = int(input("Enter the Breadth 2 : "))

obj1 = Rect(len1, bred1)
obj2 = Rect(len2, bred2)

obj1.area()
obj1.per()
obj1.display()

obj2.area()
obj2.per()
obj2.display()

obj1.compare(obj2)