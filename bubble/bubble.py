def main():
	test_cases = []
	with open("test_cases.txt", "r") as f:
		lines = f.readlines()

		for line in lines:
			test_cases.append(parseInts(line))
	print('ok')
	print(test_cases)
	print([bubble_sort(x, max) for x in test_cases])

# parse str into int array


def parseInts(s):
	return list(map(int, s.split(" ")))


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

main()
