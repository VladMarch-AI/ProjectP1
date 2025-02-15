sec = (input("Enter seconds: "))

if sec.isdigit():
    sec = int(sec)
    if 0 <= sec < 8640000:
        minutes = sec // 60
        hours = minutes // 60
        days = hours // 24
        s_n = days % 10
        f_n = days - s_n
        if 5 <= days <= 20 or s_n == 0 or 5 <= s_n:
            print(days, "Днів", end=', ')
        elif f_n == 1 or s_n == 1:
            print(days, "День", end=', ')
        else:
            print(days, "Дні", end=', ')
        print(str(hours % 24).rjust(2, '0'),
              str(minutes % 60).rjust(2, '0'),
              str(sec % 60).rjust(2, '0'),
              sep=':')
    else:
        print("Too many seconds")
else:
    print("No numbers entered or negative/fractional number")
