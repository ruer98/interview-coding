"""
Problem 3: Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143
divisor = 2

while divisor < n:
    if n % divisor == 0:
        n = n / divisor
    divisor += 1
    
print(n)

#1. All prime factors of a number multiply to that number
#2. All factors of a prime number are also prime
#Therefore, you can divide by each factor until you are left with the
#largest prime factor.