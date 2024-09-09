# Age Check
## [Video Demo](https://youtu.be/3hSIBRfEwsw)
### Description:
This program prompts the user for date of birth as an input in `Month Day, Year` format, and prints out the calculated age and days before their birthday.
#### How Does the App Operate?
The program imports the `date} object and makes use of the built-in Python library `Datetime}[^1].
Using the {.today()` class method from {date}, which has `.day{, {.month}, and {.year} instance properties, the current local date was obtained.

Additionally, the program makes use of the `re`[^2] or `regular expression` built-in Python library. This library was used to extract the necessary data and verify that the birthdate entered was formatted correctly.

Subtract the birth year from the current year to find the age.

The following variables are used in the age computations:
1. The user has not yet celebrated his or her birthday if the birthmonth is greater than the current month (for example, the birthday falls on October[10] and the current month is August [08]). Age-related deduction number one.
2. Verify whether the birthday is greater than today's day if the birthmonth and today's month are equal. In other words, if the user's birthday is on August 25 and today is August 17, then they have not yet celebrated it. Age-related deduction number one.

Subtract today's date from the birthdate in the current year to find the number of days before the birthdate (example: 2023, 10, 20 - 2023, 08, 19).
1. Add one year to the birthyear if the birthday in the current year is less than the date of today (birthdate 2023, 02, 11; today's date 2023, 08, 19). The 2024, 02, 11 - 2023, 08, 19 will be replaced by this.

### TODO:
#### Download
Download the Repository through Clone Repository or Download Zip
```
git clone https://github.com/Manixhor/age_checker.git
```
#### Installation
After download, go to `cmd` and navigate to the project folder directory.
```
cd age_checker
```
Use [pip](https://pip.pypa.io/en/stable/) to install needed libraries.
```
$ pip install -r requirements.txt
```
#### Usage
Run the program python script `project.py` with [python](https://www.python.org/).
```
python project.py
```
Test the program python script `test_project.py` with [pytest](https://docs.pytest.org/en/7.2.x/).
```
pytest test_project.py
```
After successfully running the program, it will prompt for some birthdate.
Enter the birthdate following the given format `Month Day, Year`.

![Sample Output Image](https://github.com/Manixhor/age_checker/blob/319e783d985db15353767587cb3f729e4a9d36b2/sample.jpg)

>[!NOTE]
>The program is case-insensitive.



## References
[^1]: [Datetime library](https://docs.python.org/3/library/datetime.html)
[^2]: [re library](https://docs.python.org/3/library/re.html)
