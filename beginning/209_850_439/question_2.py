import datetime
def calculate_age(year_of_birth):
    """ Calculate a person's age based on their year of birth and there age."""
    current_year = datetime.datetime.now().year
    age = current_year - year_of_birth
    return age
# Enter year of birth correctly
Dob = int(input("Enter your year of birth: "))
# Calculating age
age = calculate_age(Dob)
# Determinining if the person is over or under 18
if age > 18:
    print("You are over 18 years old.")
else:
    print("You are under 18 years old.")
    print(f'But since you are born in {Dob}, you are 18 years old')