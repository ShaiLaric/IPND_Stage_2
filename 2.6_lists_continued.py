# Mutation
# You can change the value of a list after creating it
# Strings are immutable.

p = ['H','e','l','l','o']
print p
p[0] = 'Y'

stooges = ['Moe', 'Larry', 'Curly']
stooges[2] = 'Shemp'
print stooges

# Aliasing

# When multiple variables refer to the same object,
# aliasing means that changing the value of one variable
# changes the value of the other variable[s]

spy = [0,0,7]

def replace_spy(numlist):
    numlist[2] = numlist[2]+1

replace_spy(spy)
print spy
#>>> [0,0,8]

# List Operations
# Append
# <list>.append(<element>)
# Mutates old list, doesn't create new list

stooges = ['Moe', 'Larry', 'Curly']
stooges.append('Shemp')
print stooges

# + Operator
# <list> + <list>
# [0,1]+[2,3]
# [0,1,2,3]

# Len
# len(<list>)
# Counts elements in a variable's value
