''' bubble sort implementation with arbitary sort function'''
''' sort func returns selected element, use min for min '''

def bubble_sort(x):
	for i in range(0, len(x)):
		swap = False
		for j in range(0, len(x)-1):
			if min(x[j], x[j+1]) == x[j+1]:
				tmp = x[j]
				x[j] = x[j+1]
				x[j+1] = tmp
				swap = True
		if not swap:
			break
	return x

def bubble_sort(x, sort_func):
	for i in range(0, len(x)):
		swap = False
		for j in range(0, len(x)-1):
			if sort_func(x[j], x[j+1]) == x[j+1]:
				tmp = x[j]
				x[j] = x[j+1]
				x[j+1] = tmp
				swap = True
		if not swap:
			break
	return x
