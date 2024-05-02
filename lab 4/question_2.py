"""
This program solves the palindrome problem
"""


def is_palindrome(word: str) -> bool:
    word = word.lower().replace(" ", "")
    return word == reversed(word)


user_input = input("Enter a word: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
