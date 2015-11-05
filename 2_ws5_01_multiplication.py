# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    index = 0
    answer = 1 
    
    while index < len(list_of_numbers):
        answer = answer * list_of_numbers[index]
        index += 1
    return answer

# Their way of doing it:

def product_list(list_of_numbers):
	answer = 1

	for index in list_of_numbers:
		answer = answer * index
	return answer

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1