"""calculating grades"""
def calc_grade(score):
    if 75>= score >=100:
      print('A')
    elif 65>= score >=74:
      print('B')
    elif 55>= score >=64:
      print('C')
    elif 45>= score >=54:
      print('D')
    elif 35>= score >=44:
      print('E')
    else: print('Invalid score')
    - print(f'Here is your score')