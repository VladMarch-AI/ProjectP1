numb = input("Enter number:")
if "." in numb:
    numb = numb.replace(".", "")
if "," in numb:
    numb = numb.replace(",", "")
if not numb.isdigit():
    exit("No number entered")
print(numb)