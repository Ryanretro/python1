"""
170439 Ryan Emmanuel Moshi
166010 John Mulemeoderhwa
171649 Mugisho Lubala Gideon

Here we define the work of function to be used in finding the word below code:
"""
def is_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
    print("Enter a word to check if it a palindrome: ")
    user_word = input()
    result = is_palindrome(user_word)
    print(result)