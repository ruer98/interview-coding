"""
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13. What is the 10 001st prime number?
"""

def is_prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False       
    return True
    
x = 1
i = 0

while i != 10001:
    x += 1
    if is_prime(x) == True:
        i += 1

print(x)