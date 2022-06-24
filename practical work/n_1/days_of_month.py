def days_of_month(month):
    if month.lower() == 'february':
        return 28
    elif month.lower() == "april" or month.lower() == "june" or month.lower(
    ) == "september" or month.lower() == "november":
        return 30
    else:
        return 31


month = input("enter the name of month: ")
if days_of_month(month) == 28:
    print(month, "has", "28 or 29 days")
else:
    print(month, "has", days_of_month(month), " days")
