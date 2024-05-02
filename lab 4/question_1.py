"""This program takes a range of numbers from users and lists them as either prime, odd or even. The solution is done
in each of the functions in the module."""


def is_prime(number) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_odd(number) -> bool:
    return number % 2 != 0


def is_even(number) -> bool:
    return number % 2 == 0


number_list = []

values = int(input("Enter your values, to stop enter 0: "))

while values != 0:
    number_list.append(values)
    values = int(input("Enter your values, to stop enter 0: "))

print(number_list)

odd_numbers = []
even_numbers = []
prime_numbers = []

for num in number_list:
    if is_prime(num):
        prime_numbers.append(num)
    if is_odd(num):
        odd_numbers.append(num)
    if is_even(num):
        even_numbers.append(num)

print(f'Prime Numbers are: {prime_numbers} \nEven Numbers are: {even_numbers} \nOdd Numbers are: {odd_numbers}')
