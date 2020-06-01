"""
Problem 5: Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?
"""

def isMultiple(x,n):
    for i in range(1,n):
        if x % i != 0:
            return False
    return True
    
for i in range(20, 1000000000, 20):
    if isMultiple(i,20):
        print(i)
        break

#import time
#print("Processing time: " + str(time.process_time()), "s")