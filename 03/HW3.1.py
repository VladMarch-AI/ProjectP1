first_n = input("Enter a first number: ")
second_n = input("Enter a second number: ")

if not first_n.isdigit() or not second_n.isdigit():
    exit("No numbers entered")
first_n, second_n = int(first_n), int(second_n)

sym = input("Enter a simple math operation(+, -, *, /): ")

if sym == "+":
    print(first_n + second_n)
elif sym == "-":
    print(first_n - second_n)
elif sym == "*":
    print(first_n * second_n)
elif sym == "/" and second_n != 0:
    print(first_n / second_n)
elif second_n == 0 and sym == "/":
    exit("You can't divide by 0")
else:
    exit("Invalid symbol entered")
