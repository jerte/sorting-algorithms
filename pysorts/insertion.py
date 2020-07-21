def main():
    test_cases = []
    with open("test_cases.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            test_cases.append(parseInts(line))
    print(test_cases)
    print([insertion_sort(x, max) for x in test_cases])

# parse str into int array
def parseInts(s):
    return list(map(int, s.split(" ")))

def insertion_sort(x, sort_func):
	for i in range(1, len(x)):
		key = x[i]
		j = i - 1
		while j>=0 and sort_func(x[j], key)==key:
			x[j + 1] = x[j]
			j -= 1
		x[j + 1] = key

	return x


main()
