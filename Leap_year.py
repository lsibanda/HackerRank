def leapYear(year):
    isLeap = False

    if year % 400 == 0:
        isLeap = True
    elif year % 100 == 0:
        isLeap = False
    elif year % 4 == 0:
        isLeap = True

    return isLeap

year = int(input())
print leapYear(year)
