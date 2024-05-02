"""
170439 Ryan Emmanuel Moshi
166010 John Mulemeoderhwa
171649 Mugisho Lubala Gideon

Here we define the work of function to be used in finding the word below code:
"""
import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def categorize_numbers():
    primes = []
    odds = []
    evens = []

    while True:
        num = int(input("Enter a number (enter 0 to stop): "))
        if num == 0:
            break
        if is_prime(num):
            primes.append(num)
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    print("Prime numbers are:", primes)
    print("Odd numbers are:", odds)
    print("Even numbers are:", evens)

categorize_numbers()

