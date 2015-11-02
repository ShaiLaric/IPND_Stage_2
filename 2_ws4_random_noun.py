# randint

from random import randint	# randint isn't in base Python

# randint(low, high)	# returns a number from low to high, inclusive

def random_noun():
	random_num = randint(0,1)
	if random_num == 0:
		return "sofa"
	return "llama"

def random_verb():
	random_verb = randint(0,1)
	if random_verb == 0:
		return "run"
	return "kayak"



i = 0
while i < 10:
	print random_noun() + " likes to " + random_verb()
	i += 1
