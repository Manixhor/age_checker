from project import parse_date_input, month_name_to_number, compute_age, days_until_next_birthday
from datetime import date
import pytest

def test_parse_date_input():
    assert parse_date_input("October 20, 2000") == ('october', '20', '2000')
    assert parse_date_input("nov 02, 2001") == ('nov', '02', '2001')

def test_parse_date_input_valueerror():
    with pytest.raises(ValueError):
        parse_date_input("October 20 2000")
    with pytest.raises(ValueError):
        parse_date_input("Septembers 05, 2003")
    with pytest.raises(ValueError):
        parse_date_input("jan 34, 2005")
    with pytest.raises(ValueError):
        parse_date_input("Feb 11, 200")

def test_month_name_to_number():
    assert month_name_to_number("october") == 10
    assert month_name_to_number("nov") == 11

def test_month_name_to_number_valueerror():
    with pytest.raises(ValueError):
        month_name_to_number('Septembers')
    with pytest.raises(ValueError):
        month_name_to_number('febraury')  # Note: 'febraury' should be 'february'

def test_compute_age():
    today = date.today()
    # Adjust the expected result based on today's date
    assert compute_age("october", 20, 2000, today) == today.year - 2000 - (1 if (month_name_to_number("october") > today.month or (month_name_to_number("october") == today.month and 20 > today.day)) else 0)
    assert compute_age("nov", 2, 2001, today) == today.year - 2001 - (1 if (month_name_to_number("nov") > today.month or (month_name_to_number("nov") == today.month and 2 > today.day)) else 0)

def test_days_until_next_birthday():
    today = date.today()
    # Calculate the number of days until the next birthday
    oct_20_this_year = date(today.year, month_name_to_number("october"), 20)
    if oct_20_this_year < today:
        oct_20_this_year = oct_20_this_year.replace(year=today.year + 1)
    expected_days_until_oct_20 = (oct_20_this_year - today).days
    assert days_until_next_birthday("october", 20, today) == expected_days_until_oct_20

    nov_2_this_year = date(today.year, month_name_to_number("nov"), 2)
    if nov_2_this_year < today:
        nov_2_this_year = nov_2_this_year.replace(year=today.year + 1)
    expected_days_until_nov_2 = (nov_2_this_year - today).days
    assert days_until_next_birthday("nov", 2, today) == expected_days_until_nov_2
