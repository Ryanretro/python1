"""
Ryan Emmanuel Moshi - 170439
Mohammed Hassan Ally - 172229
"""
"""
This a python code which is used to print out the score and the corresponding grade for the student
The score must be between 0 and 100 and also in numerical range only otherwise it will be invalidated
A user must prompt for the score otherwise the grade will not be displayed
"""
def calculate_grade(score):
    if 75 <= score <= 100:
        return 'A'
    elif 60 <= score <= 74:
        return 'B'
    elif 50 <= score <= 59:
        return 'C'
    elif 40 <= score <= 49:
        return 'D'
    elif 0 <= score <= 39:
        return 'F'
    else:
        return 'Invalid'
def main():
    try:
        score = float(input("Enter the student's score: "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"Score: {score}\nGrade: {grade}")
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric score.")

if __name__ == "__main__":
    main() 