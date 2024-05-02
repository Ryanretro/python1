import datetime

def calculate_age(year_of_birth):
    """ Calculate a person's age based on their year of birth and there age.
    Args:
        year_of_birth (int): The year of birth.
    Returns:
        int: The person's age.
    """
    current_year = datetime.datetime.now().year
    age = current_year - year_of_birth
    return age
# Enter year of birth correctly
year_of_birth = int(input("Enter your year of birth: "))
# Calculating age
age = calculate_age(year_of_birth)
# Determinining if the person is over or under 18
if age >= 18:
    print("You are over 18 years old.")
else:
    print("You are under 18 years old.")