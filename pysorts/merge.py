def main():
	test_cases = []
	with open("test_cases.txt", "r") as f:
		lines = f.readlines()

		for line in lines:
			test_cases.append(parseInts(line))
	print(test_cases)
	for x in test_cases:
		merge_sort(x, min, 0, len(x)-1)
	print(test_cases)

# parse str into int array
def parseInts(s):
	return list(map(int, s.split(" ")))

def merge_sort(x, sort_func, left, right):
	if right > left:
		mid = int((left+right)/2)
		
		merge_sort(x, sort_func, left, mid)
		merge_sort(x, sort_func, mid+1, right)

		merge(x, sort_func, left, mid, right)	

def merge(x, sort_func, left, mid, right):
	i = left
	left = x[left:mid+1]
	right = x[mid+1:right+1]
	left_i = 0
	right_i = 0
	
	while(left_i < len(left) and right_i < len(right)):
		if sort_func(left[left_i], right[right_i])==left[left_i]:
			x[i] = left[left_i]
			left_i+=1
			i+=1
		else:
			x[i] = right[right_i]
			right_i+=1
			i+=1
		

	while left_i < len(left):
		x[i] = left[left_i]
		left_i+=1
		i+=1
	while right_i < len(right):
		x[i] = right[right_i]
		right_i+=1
		i+=1
	
main()
