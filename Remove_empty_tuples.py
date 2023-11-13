# Python program to remove empty tuples from a given list of tuples

def Remove1(tuples):
	tuples = [t for t in tuples if t]
	return tuple(tuples)

tuples = ((), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'),())
print(Remove1(tuples))
