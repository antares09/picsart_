def check_season(month):
    if month.lower() == "april" or month.lower() == "march" or month.lower(
    ) == "may":
        return "spring"
    elif month.lower() == "september" or month.lower(
    ) == "november" or month.lower() == "october":
        return "outumn"
    elif month.lower() == "june" or month.lower() == "july" or month.lower(
    ) == "august":
        return "summer"
    else:
        return "winter"


month = input("enter name of month: ")
day = int(input("enter the day: "))

print(month, day, "is ", check_season(month))
