# We now would like to summarize this data and make it more visually appealing
# We want to go through count_list and print a table that shows the number and its 
# corresponding count.

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""
# Here is our code we have written so far:

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

# Aggregate the data -------------------------------------------------
count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

print "number | occurrence"
index = 0
numlength = len("number")

while index < len(count_list):
    numspace = numlength - len(str(index))
    print " " * numspace + str(index) + " | " + str(count_list[index])
    index +=1

print ""
print random_list

    
# BONUS!
# From your summarize code you just wrote, can you make the table even more visual by 
# replacing the count with a string of asterisks that represent the count of a number?
# The table should look like

"""
number | occurrence
     0 | *
     1 | **
     2 | ***
     3 | **
     4 | **
     5 | *
     6 | *
     7 | **
     8 | ***
     9 | *
    10 | **
"""
print ""
print "number | occurrence"

index = 0
numlength = len("number")

while index < len(count_list):
    numspace = numlength - len(str(index))
    print " " * numspace + str(index) + " | " + "*" * count_list[index]
    index +=1

# Congratulations! You just created a distribution table of a list of numbers! 
# This is also known as a histogram