days = input("Enter the number of days: ")
hours = input("Enter the number of hours: ")
mint = input("Enter the number of minutes: ")
sec = input("Enter the number of seconds: ")
lst = [days, hours, mint, sec]
for _ in lst:
    if not _.isdigit():
        exit("No numbers entered")
days, hours, mint, sec = int(days), int(hours), int(mint), int(sec)
print(days * 24 + hours * 3600 + mint * 60 + sec)
