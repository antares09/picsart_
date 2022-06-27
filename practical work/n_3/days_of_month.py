def month_days(year, month):
    if month.lower() == 'february':
        if year % 4 == 2:
            return 28
        else:
            return 29
    elif month.lower() == "april" or month.lower() == "june" or month.lower(
    ) == "september" or month.lower() == "november":
        return 30
    else:
        return 31


year = int(input("enter the year: "))
month = input("enter the name of month: ")
print(year, month, "has", month_days(year, month), " days")
