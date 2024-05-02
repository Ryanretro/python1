"""
This python module uses the least python knowledge to calculate the age of a person
"""

# in this solution, it would be good to take the persons year of birth. Then also use the age date module
import datetime

# below is the current year, 2023 in this case
current_year = datetime.datetime.now().year

dob = int(input('What is your year of Birth? '))

age = int(current_year - dob)

if age > 18:
    print('you are over 18')
else:
    print('you are under 18')

print(f'Since you were born in {dob}, your age is {age}')
