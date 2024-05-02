"""Joshua Onsongo - 171772
   Ryan Moshi - 170439
"""
#we first define the numbers to be used in the array and the integer target
def arraynum(numbers, target):
    #we then define the numbers according to their function
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [numbers[i], numbers[j]]
    return []
#we then list the numbers and initialize our target
numbers = [2, 7, 11, 15]
target = 13
#lastly we print out the output
print(arraynum(numbers, target))