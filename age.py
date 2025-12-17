from datetime import datetime


def calculate_age(date_string):
    # converts input string (dd-mm-yyyy) into a datetime object
    birth_date = datetime.strptime(date_string, "%d-%m-%Y")
    today = datetime.today()

    # difference in years
    age = today.year - birth_date.year

    # if birthday hasn’t happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


# Examples
print(calculate_age("01-01-1990"))
print(calculate_age("26-11-1972"))
