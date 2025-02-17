first_n = input("Enter a first number: ")
second_n = input("Enter a second number: ")

if not first_n.isdigit() or not second_n.isdigit():
    exit("No numbers entered")
first_n, second_n = int(first_n), int(second_n)

print("Sum: ", first_n + second_n)
print("Difference: ", first_n - second_n)
print("Product: ", first_n * second_n)
print("Division: ", first_n / second_n)
print("Remainder of division: ", first_n % second_n)
print("The first number to the power of the second number: ",
      first_n ** second_n)
