"""
This module grades the scores entered by the student
"""
score = float(input('Enter your score '))

if score > 100:
    print(f'Your score of {score} is Out of Bound')
elif score >= 75:
    print(f'Your score of {score} is grade A')
elif score >= 60:
    print(f'Your score of {score} is grade B')
elif score >= 50:
    print(f'Your score of {score} is grade C')
elif score >= 40:
    print(f'Your score of {score} is grade D')
elif score >= 0:
    print(f'Your score of {score} is grade E')
else:
    print(f'Your score of {score} is Invalid')

