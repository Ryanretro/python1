"""This python module calculates the prime numbers given two points while using very basic knowledge"""

start = int(input('Enter the start of the range '))
stop = int(input('Enter the end of the range '))

# now let us get the prime numbers
for val in range(start, stop + 1):
    if val > 1:
        for i in range(2, val):
            if (val % i) == 0:
                break
        else:
            print(val, end=" ")


