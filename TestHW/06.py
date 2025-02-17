a = input("Enter True or False: ")
b = input("Enter True or False: ")

if a == "True":
    a = True
if a == "False":
    a = False
if b == "True":
    b = True
if b == "False":
    b = False

print("1.", a and b)
print("2.", a or b)
print("3.", not a)
print("4.", not b)
print("5.", a == b)
print("6.", a != b)
