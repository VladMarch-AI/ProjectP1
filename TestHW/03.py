from math import pi

rad = input("Enter the radius of the circle:")
if "." in rad:
    rad = rad.replace(".", "")
if "," in rad:
    rad = rad.replace(",", "")
if not rad.isdigit():
    exit("No numbers entered")

rad = float(rad)
circuit = 2 * pi * rad
area = pi * rad ** 2

print("Circuit: ", circuit)
print("Area of a circle: ", area)
