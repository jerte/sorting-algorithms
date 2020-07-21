''' selection sort implementation with arbitrary sort function '''
''' sort func returns selected element, use min for min '''

def selection_sort(x, sort_func):
	if(len(x) <= 1):
		return x
	else:
		insert_index = 0
		while(insert_index < len(x)-1):
			e = insert_index
			
			for i in range(insert_index+1, len(x)):
				if(sort_func(x[i], x[e])==x[i]):
					e = i

			if(e != insert_index):
				swp = x[insert_index]
				x[insert_index] = x[e]
				x[e] = swp
						
			insert_index += 1
	return x
