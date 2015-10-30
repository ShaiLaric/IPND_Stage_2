# Lesson 2.4: Making Decisions - If Statements
# Final Quiz

def biggest(a, b, c):
	if a >= b and a >= c:
		return a
	if b >= a and b >= c:
		return b
	else:
		return c

# Redefined below with Dave's solution:

def biggest(a, b, c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

print biggest(3, 6, 9)
print biggest(9, 3, 6)
print biggest(3, 3, 9)
print biggest(9, 3, 9)
# mine next
print biggest(1, 2, 3)
print biggest(4, 2, 2)
print biggest(6, 5, 6)
print biggest(5, 6, 5)