"""This python module shows the most basic solution to question one."""

# part B of the question is solved below
string_value = 'This is Samsung'
print(f'The original string values is {string_value}', end=' ')

# below, we are now changing the string value to another value
string_value = 'This is Apple'
print(f'and the new string value is {string_value}\n\nNow let us Work on the cone\n')

# below is the code for calculating the area and the volume of a cone.
PI = 3.142
base_radius = 10
slant_height = 20

base_area = (PI * base_radius ** 2)
slant_area = (PI * base_radius * slant_height)
total_area = base_area + slant_area

# Calculating the volume
volume = ((1 / 3) * PI * base_radius ** 2 * slant_height)

# printing out the results
print(f'The Area of the Cone is {round(total_area, 2)} and the volume is {round(volume, 2)}')



string_value = 'This is Apple'
print(f'The original string values is {string_value}', end=' ')

# below, we are now changing the string value to another value
string_value = 'This is Samsung'
print(f'and the new string value is {string_value}\n\nNow let us Work on the cone\n')