numb = input("Enter the radius of the circle:")
if "." in numb:
    numb = numb.replace( ".", "")
if "," in numb:
    numb = numb.replace( ",", "")
if not numb.isdigit():
    exit("No numbers entered")
print(numb)