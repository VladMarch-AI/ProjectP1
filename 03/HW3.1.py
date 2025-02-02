a = input("Enter a first number: ")
b = input("Enter a second number: ")

if not a.isdigit() or not b.isdigit():
    exit("No numbers entered")

sym = input("Enter a simple math operation(+, -, *, /): ")

if sym == "+":
    print(int(a)+int(b))
elif sym == "-":
    print(int(a)-int(b))
elif sym == "*":
    print(int(a)*int(b))
elif sym == "/" and int(b) != 0:
    print(int(a)/int(b))
elif int(b) == 0 and sym == "/":
    exit("You can't divide by 0")
else:
    exit("Invalid symbol entered")

