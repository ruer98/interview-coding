"""
Problem 28: Number spiral diagonals
Starting with the number 1 and moving to the right in a clockwise 
direction a 5 by 5 spiral is formed as follows: ...
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sume of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""

#creates 2-d spiral list
def spiral(n):
    #makes n x n matrix full of zeros
    spiral = [[0 for x in range(n)] for y in range(n)]
    #set starting number
    num = 1
    #starting position
    x = y = n // 2
    
    #fills in middle point of matrix
    spiral[y][x] = num
    num += 1
    
    for i in range(1,n):       
        #first part of spiral
        if i % 2 != 0:     
            #move right one step
            x += 1
            spiral[y][x] = num
            num +=1
            #move down i steps
            for j in range(i):
                y += 1
                spiral[y][x] = num
                num += 1
            #move left i steps
            for j in range(i):
                x -= 1
                spiral[y][x] = num
                num += 1
        #second part of spiral
        else:
            #move left one step
            x -= 1
            spiral[y][x] = num
            num += 1
            #move up i steps
            for j in range(i):
                y -= 1
                spiral[y][x] = num
                num += 1
            #move right i steps
            for j in range(i):
                x += 1
                spiral[y][x] = num
                num += 1
    
    return spiral

spiral = spiral(1001)

#diagonal 1 sum
x = y = 0
diag1 = 0
for i in range(len(spiral)):
    diag1 += spiral[y][x]
    x += 1
    y += 1 
    
#diagonal 2 sum
x = 0
y = len(spiral) - 1
diag2 = 0
for i in range(len(spiral)):
    diag2 += spiral[y][x]
    x += 1
    y -= 1
    
sum = diag1 + diag2 - 1 #diagonals intersect at 1
print(sum)