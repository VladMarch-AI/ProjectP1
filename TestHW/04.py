x1 = float(input("Enter the coordinates "'x'" of the first point: "))
y1 = float(input("Enter the coordinates "'y'" of the first point: "))
x2 = float(input("Enter the coordinates "'x'" of the second point: "))
y2 = float(input("Enter the coordinates "'y'" of the second point: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance:", distance)
