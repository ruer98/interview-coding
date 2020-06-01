"""
Problem 112: Bouncy Numbers
Working from left-to-right if no digit is exceeded by the digit to its 
left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is 
called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor 
decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, 
but just over half of the numbers below one-thousand (525) are bouncy. 
In fact, the least number for which the proportion of bouncy numbers 
first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the 
time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is 
exactly 99%.
"""

def is_bouncy(num):
    incr = False
    decr = False
    right_dig = num % 10
    num = num // 10
    while num > 0:
        left_dig = num % 10
        if left_dig < right_dig:
            incr = True
        elif left_dig > right_dig:
            decr = True
        right_dig = left_dig
        num = num // 10
        if incr and decr:
            return True
    return False
    
count = 0
i = 99 #starting point, since <100 can't be bouncy
while (count < .99 * i): #count less than 99% of total
    i += 1
    if is_bouncy(i):
        count += 1
        
print(i)
    