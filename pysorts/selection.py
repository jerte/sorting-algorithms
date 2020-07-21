def main():
	test_cases = []
	with open("test_cases.txt", "r") as f:
		lines = f.readlines()

		for line in lines:
			test_cases.append(parseInts(line))
	print(test_cases)
	print([selection_sort(x, max) for x in test_cases])

# parse str into int array
def parseInts(s):
	return list(map(int, s.split(" ")))


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

main()
