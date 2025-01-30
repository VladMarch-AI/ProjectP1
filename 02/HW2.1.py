abcd = int(input("Enter a four-digit number: "))

print(abcd // 1000)
a = int(abcd // 1000)
print(abcd // 100 - a * 10)
b = int(abcd // 100 - a * 10)
print(abcd // 10 - (a * 100 + b*10))
c = int(abcd // 10 - (a * 100 + b*10))
print(abcd // 1 - (a*1000 + b*100 + c*10))
