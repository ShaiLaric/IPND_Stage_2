def bigger (a, b):
	if a > b:
		return a
	else:
		return b

def biggest (a, b, c):
	return bigger(bigger(a,b), c)

def median(a, b, c):
	if biggest(a, b, c) == a:
		if bigger(b, c) == b:
			return b
		return c
	if biggest(a, b, c) == b:
		if bigger(a, c) == a:
			return a
	return b

# Second Try
def median(a, b, c):
	if biggest(a, b, c) == a:
		return bigger(b, c)
	if biggest(a, b, c) == b:
		return bigger(a, c)
	if biggest(a, b, c) == c:
		return bigger(a, b)

def median(a, b, c):
	big = biggest(a, b, c)
	if big == a:
		return bigger(b, c)
	if big == b:
		return bigger(a, c)
	return bigger(a, b)

print median(1,2,3)		#2
print median(9,3,6)		#6
print median(7,8,7)		#7
print median(12,12,9)	#12
print median(2,6,1)		#2
print median(2,1,3)		#2