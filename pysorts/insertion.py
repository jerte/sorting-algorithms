''' insertion sort implementation with arbitary sort function '''
''' sort func returns selected element, use min for min'''

def insertion_sort(x, sort_func):
	for i in range(1, len(x)):
		key = x[i]
		j = i - 1
		while j>=0 and sort_func(x[j], key)==key:
			x[j + 1] = x[j]
			j -= 1
		x[j + 1] = key

	return x
