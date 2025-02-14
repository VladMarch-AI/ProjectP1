while True:
    ans = str.lower(input("Do you want start? : "))
    if ans in ['y', 'yes', 'т', 'так', 'д', 'да']:
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
