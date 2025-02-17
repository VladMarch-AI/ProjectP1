from math import pi

rad = input("Enter the radius of the circle:")
if rad == int(rad) or rad == float(rad):
    exit("No numbers entered")
rad = int(rad)
circuit = 2 * pi * rad
area = pi * rad ** 2

print("Circuit: ", circuit)
print("Area of a circle: ", area)
