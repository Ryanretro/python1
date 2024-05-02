'''Joshua Onsongo-171772
   Ryan Moshi-170439
'''
import re
student_names = ['Amanda Talib', 'Susan St. James', 'Andréas Gor', 'örjan Lewis']
# Define the letters and symbols to be used to find the characters
special_characters_pattern = re.compile(r'[^a-zA-Z0-9\s]+')
# This code below will print the names of the special characters only
special_character_names = [name for name in student_names if special_characters_pattern.search(name)]
for name in special_character_names:
    print("1.Name " + name)