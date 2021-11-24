
# =============================================== HOMEWORK-1 =======================================================
# ==================================================================================================================


# =============================================== TASK-4 ===========================================================

""" 
Write a function that takes a string object as parameter and returns the reversed version of the string.
For this task, you should use only the built-in data types and functions.
"""

# Answer for Task-4:

def reverse(string):
    
    reverseOfString = ""
    
    for i in range(1, len(string)+1):
        reverseOfString = reverseOfString + string[-i]
        
    return reverseOfString


# ====================================================== TASK-5 ====================================================

"""
R-1.2: Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

# Answer for R-1.2:

def is_even(k):

    while k > 0:
        k -= 2
        
    if k == 0:
        return True
    else:
        return False

"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

# Answer for R-1.6:

def squares(n):

    sumOfSquares = 0
    
    for i in range(n):
        if i % 2 == 1:
            sumOfSquares += i ** 2
            
    return sumOfSquares

"""
R-1.7 Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function.
"""

# Answer for R-1.7:

def squaresAlternative(n):
    
    return sum([i**2 for i in range(n) if i%2 == 1])

"""
R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

# Answer for R-1.9:

list = []
for i in range(50, 81, 10):
    list.append(i)
print(list)

"""
R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

# Answer for R-1.11:

list = [2 ** n for n in range(0, 9)]
print(list)

"""
C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

# Answer for C-1.19:

alphabet_list = [chr(i) for i in range(ord("a"), ord("z")+1)]
print(alphabet_list)

"""
C-1.20 Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible order 
occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

# Answer for C-1.20:

from random import randint

def shuffle(data):
    
    data2 = []
    length = len(data)

    for i in range(0, length):
        randomInteger = randint(0, length-1-i)
        tmp = data[randomInteger]
        data2.append(tmp)
        del data[randomInteger]
        del tmp
    data = data2
    
    return data
    

"""
C-1.28 For the special case of p = 2, this results in the traditional Euclidean norm, 
which represents the length of the vector. For example, the Euclidean norm of a 
two-dimensional vector with coordinates (4,3) has a Euclidean norm of 
sqrt(4^2 +3^2) = sqrt(16+9) = sqrt(25) = 5. Give an implementation of a function 
named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers
"""

# Answer for C-1.28:

from math import sqrt

def norm(v, p=None):
    
    lengthOfList = len(v)
    sum = 0
    
    if p == None:
        p = 2
    else:
        p = p
    
    for i in range(0, lengthOfList):
        sum = sum + v[i] ** p
        
    return sqrt(sum)
 
# =============================================== TASK-6 ==================================================
 
"""
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100.
"""

# Answer for C-1.35:

from random import randint

# the list of number of persons to simulate
testList = [i for i in range(5, 101, 5)]

# the function to calculate probability
def probability(sum, total):
    return sum / total

# Monte Carlo Simulation function
def monteCarlo(numberOfPerson):

    # Number of how many times 2 or more people have the same birthday
    sum = 0

    # Simulation with 1000 iterations
    for i in range(0, 1000):

        # List of birthdays of people
        birthdayList = []

        # Another iteration for number of people to choose the birthdays
        for i in range(0, numberOfPerson):

            # Random birthday generation of people
            random = randint(0, 365)

            # An if statement that can consider the same birthdays
            # If a new generated birthday is in the list, then loop breaks
            if random in birthdayList:
                sum = sum + 1
                break

            # If there is no same birthday number in the list, the new one added
            else:
                birthdayList.append(random)
                
    # Final probability return using probability() function
    return probability(sum, 1000)

# The function that can perform previous functions(monteCarlo() and
# probability())in the list        
def simulation(list):

    # The list that will show the different probabilities in terms of
    # different number of people in the list
    probabilityList = []

    # For loop to perform different number of people in the list
    for i in list:

        # Produces probabilities and appending in the new list
        probabilities = round(monteCarlo(i), 2)
        probabilityList.append(probabilities)
        
    return probabilityList

print(simulation(testList))


# ==================================================== TASK-7 ========================================================

while len(l1) != 0:
    l2.insert(len(l2), 11.pop(0))

# Firstly pop() method removes the index of a list and insert() method takes an index to a specific position.
# In this piece of code the position of index that are inserted is len(l2) which is a new position right after the own indices.
# These operations should be continue until whole indices of l1 are removed fromthe list.
# Finally, l1 is an empty list and l2 is the list with its indices and the indices from l1 orderly.

# =====================================================================================================================
