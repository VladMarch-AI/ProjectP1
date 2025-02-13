while True:
    ans = str(input("Do you want start? ('y' or 'yes' for start) : "))
    if ans.startswith("y") or ans.startswith("yes"):
        first_n = input("Enter a first number: ")
        second_n = input("Enter a second number: ")

        if not first_n.isdigit() or not second_n.isdigit():
            print("No numbers entered")
            continue
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
            print("You can't divide by 0")
            continue
        else:
            print("Invalid symbol entered")
            continue
    else:
        exit("Good bye")
