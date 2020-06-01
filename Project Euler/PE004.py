"""
Problem 4: Largest Palindrome Product
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

n = 0

#a and b are the two multiplied numbers
for a in range(100, 1000):
    for b in range(100, 1000):
        x = a * b
        if x > n:
            if str(x) == str(x)[::-1]:
                n = x
print(n)
