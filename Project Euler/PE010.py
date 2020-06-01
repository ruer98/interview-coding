"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def is_prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False       
    return True
    
i = 2
sum = 0

while i < 2000000:
    if is_prime(i) == True:
        sum += i
    i += 1

print(sum)

#import time
#print("Processing time: " + str(time.process_time()), "s")