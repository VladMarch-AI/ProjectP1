abcde = int(input("Enter a five-digit number: "))

a = int(abcde // 10000)
b = int(abcde // 1000 - a * 10)
c = int(abcde // 100 - (a * 100 + b*10))
d = int(abcde // 10 - (a*1000 + b*100 + c*10))
e = int(abcde // 1 - (a*10000 + b*1000 + c*100 + d*10))

abcde_mirror = (a + b*10 + c*100 + d*1000 + e*10000)
print(abcde_mirror)
