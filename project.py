"""
NAME
    Age Checker

DESCRIPTION
    This program prompts the user for date of birth as an input in (Month Day, Year) format, and returns
    the calculated age and days before their birthday.

FUNCTIONS
    is_valid(birthdate: str)
        Returns the checked format of birthday.
    month_to_integer(month: str)
        Returns the equivalent integer of the month.
    calculate_age(birthmonth: str, birthday: int, birthyear: int, today)
        Returns the age, and the number of days before birthday.
    calculate_days(birthday: int, birthmonth: str, today)
        Returns the number of days before birthday.
"""

from datetime import date
import re


def main():
    month_name, day, year = parse_date_input(input("Enter your birthdate (e.g., January 1, 2000): ").lower())
    today = date.today()
    age = compute_age(month_name, int(day), int(year), today)
    days_until_birthday = days_until_next_birthday(month_name, int(day), today)
    print(f"Your age as of {today.strftime('%B %d, %Y')} is {age} years old.")
    print(f"There are {days_until_birthday} days until your next birthday!")


def parse_date_input(date_string: str):
    """
    Validates and parses the birthdate input.

    Args:
        date_string (str): The string to validate and parse.

    Returns:
        tuple: A tuple containing the month name, day, and year.

    Raises:
        ValueError: If the input format is invalid.
    """
    pattern = r"^([a-z]{3,9})\s([0-2]?[0-9]|3[0-1]),\s?([0-9]{4})$"
    match = re.search(pattern, date_string, re.IGNORECASE)
    if match:
        return match.group(1), match.group(2), match.group(3)
    else:
        raise ValueError("Invalid date format.")


def month_name_to_number(month_name: str):
    """
    Converts the full or abbreviated month name to its corresponding integer.

    Args:
        month_name (str): The full or abbreviated name of the month.

    Returns:
        int: The month number (1-12).

    Raises:
        ValueError: If the month name is not recognized.
    """
    month_map = {
        "full": {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "july": 7,
            "august": 8,
            "september": 9,
            "october": 10,
            "november": 11,
            "december": 12,
        },
        "abbreviated": {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12,
        },
    }
    if month_name in month_map["full"]:
        return month_map["full"][month_name]
    elif month_name in month_map["abbreviated"]:
        return month_map["abbreviated"][month_name]
    else:
        raise ValueError("Month name not recognized.")


def compute_age(month_name: str, day: int, year: int, current_date):
    """
    Calculates the age based on the birthdate and the current date.

    Args:
        month_name (str): The name of the birth month.
        day (int): The birth day.
        year (int): The birth year.
        current_date (datetime.date): The current date.

    Returns:
        int: The calculated age.
    """
    age = current_date.year - year
    if month_name_to_number(month_name) > current_date.month:
        age -= 1
    elif month_name_to_number(month_name) == current_date.month:
        if day > current_date.day:
            age -= 1

    return age


def days_until_next_birthday(month_name: str, day: int, current_date):
    """
    Calculates the number of days until the next occurrence of the birthday.

    Args:
        month_name (str): The name of the birth month.
        day (int): The birth day.
        current_date (datetime.date): The current date.

    Returns:
        int: The number of days until the next birthday.
    """
    birthday_this_year = date(current_date.year, month_name_to_number(month_name), day)
    if birthday_this_year < current_date:
        birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
    days_until_birthday = (birthday_this_year - current_date).days

    return days_until_birthday


if __name__ == "__main__":
    main()
