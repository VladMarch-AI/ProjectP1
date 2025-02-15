from string import ascii_letters

ans = (input("Enter two liters ( _ - _ ): "))
_ = ans.split(sep="-")

first_let = ascii_letters.index(_[0])
second_let = ascii_letters.index(_[1])

first_let -= 1
while first_let < second_let:
    first_let += 1
    print(ascii_letters[first_let], end='')
