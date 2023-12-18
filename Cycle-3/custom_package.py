from Graphics.DGraphics import cuboid, sphere
from Graphics import circle, rectangle

print("---------Circle---------")
r = int(input("Enter radius of circle : "))
print("Area of circle : ", circle.areac(r))
print("Perimeter of circle : ", circle.perc(r))

print("---------Rectangle---------")
len = int(input("Enter the length : "))
brth = int(input("Enter the breadth : "))
print("Area of rectangle : ", rectangle.arear(len, brth))
print("Perimeter of rectangle : ", rectangle.perr(len, brth))

print("---------Cuboid---------")
len1 = int(input("Enter the length : "))
brth1 = int(input("Enter the breadth : "))
height1 = int(input("Enter the height : "))
print("Area of cuboid : ", cuboid.areacb(len1, brth1, height1))
print("Perimeter of cuboid : ", cuboid.percb(len1, brth1, height1))

print("---------Sphere---------")
rad = int(input("Enter the radius : "))
print("Area of sphere : ", sphere.areasp(rad))
print("Perimeter of sphere : ", sphere.persp(rad))