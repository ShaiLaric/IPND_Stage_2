# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

#def count():
#    i = 0
#    while i < 10:
#        print i
#        i = i + 1

# count()

# Add your own code and notes here

#def count():
#    i = 0
#    while i < 10:
#        print i
#        i += 1		# Testing += to increment counter

#count()

# While loops
#
# while <test expression>:
#	block
#
# If executes 0 or 1 times.

#i = 1
#while 1 != 10:
#	i = i+2
#	print i

# The above runs forever or until memory runs out.

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints out
# all the whole numbers from 1 to the input number.

# Make sure your procedure prints "upwards", from
# 1 up to the input number.

def print_numbers(orig_num):
	num = 1
	while num <= orig_num:
		print num
		num += 1

print_numbers(3)

# Break Time!
#
# while <test expression>:
#	<code>
#	if <BreakTest>:
#		break
#	<more code>
#
# <post-while code>

def print_numbers(orig_num):
	num = 1
	while True:
		if num > orig_num:
			break
		print num
		num += 1

print_numbers(3)