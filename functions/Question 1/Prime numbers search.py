"""
Ryan Emmanuel Moshi - 170439
Mohammed Hassan Ally - 172229
"""
"""
This a python code which is used to printout prime numbers in a given range that the user wants.
The starting number will be inclusive and the ending number will be exclusive
The starting number must not be greater than the ending number
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
if start >= end:
    print("Invalid range. The starting number must be less than the ending number.")
else:
    print(f"Prime numbers between {start} and {end} are")
    for num in range(start, end):
        if is_prime(num):
            print(num)