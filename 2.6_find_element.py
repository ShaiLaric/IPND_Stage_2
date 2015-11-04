def find_element(input_list, some_value):
	i = 0
	for e in input_list:
		if e == some_value:
			return i
		i += 1
	return -1


#print find_element([1,2,3],3)
#>>> 2
#print find_element([3,2,1],3)
#print find_element(['alpha','beta'],'gamma')
#>>> -1

def find_element(input_list, some_value):
	for e in input_list:
		if e == some_value:
			return input_list.index(e)
	return -1


def find_element(input_list, some_value):
	if some_value in input_list:
		return input_list.index(some_value)
	else:
		return -1

print find_element([1,2,3],3)
print find_element([3,2,1],3)
print find_element(['alpha','beta'],'gamma')
