class custom_sort_list(list):
	# to do later, support types other than list
	def __init__(self, data):
		super().__init__(data)
		self.__supported_algos = ['bubble', 'insertion', 'selection',
									'merge', 'quick', 'quicksort']
	 
	def sort(self, **args):
		if 'algo' in args:
			if args['algo'] in self.__supported_algos:
				getattr(self, args['algo']+"_sort")()
		else:
			return super().sort()

	''' merge sort '''
	def merge(self, left, mid, right):

		i = left
		left_i = 0
		right_i = 0
		
		left = self[left:mid+1]
		right = self[mid+1:right+1]

		while left_i < len(left) and right_i < len(right):
			if left[left_i] < right[right_i]:
				self[i] = left[left_i]
				left_i += 1
			else:
				self[i] = right[right_i]
				right_i += 1
			i += 1

		while left_i < len(left):
			self[i] = left[left_i]
			left_i += 1
			i += 1
		while right_i < len(right):
			self[i] = right[right_i]
			right_i += 1
			i += 1

	def merge_sort(self, left=0, right=None):
		if right==None: 
			right = len(self)-1
		if right > left:
			mid = int((left+right)/2)
			self.merge_sort(left, mid)
			self.merge_sort(mid+1, right)
			self.merge(left, mid, right)
	
	''' quick sort '''
	def partition(self, left, right):
		pivot = self[right]
		i = left-1

		for j in range(left, right):
			if self[j] < pivot:
				i += 1
				self[i], self[j] = self[j], self[i]
		self[i+1], self[right] = self[right], self[i+1]
		return i+1
	
	def quick_sort(self, left=0, right=None):
		if right==None:
			right = len(self)-1
		if right > left:
			i = self.partition(left, right)
			self.quick_sort(left, i-1)
			self.quick_sort(i+1, right) 
	
	def quicksort_sort(self):
		return self.quick_sort(0, len(self)-1)

	''' insertion sort '''
	def insertion_sort(self):
		for i in range(1, len(self)):
			key = self[i]
			j = i - 1
			while j >= 0 and self[j] > key:
				self[j+1] = self[j]
				j -= 1
			self[j + 1] = key
	
	''' selection sort '''
	def selection_sort(self):
		for i in range(0, len(self)):
			min_index = i
			for j in range(i, len(self)):
				if self[j] < self[min_index]:
					min_index = j
			self[min_index], self[i] = self[i], self[min_index]
	
	''' bubble sort '''
	def bubble_sort(self):
		for i in range(0, len(self)):
			swp = False
			for j in range(0, len(self)-1):
				if self[j+1] < self[j]:
					self[j+1], self[j] = self[j], self[j+1]
					swp = True
			if not swp:
				break


import unittest
from random import randint

def make_randints(x):
	for i in range(0, x):
		yield randint(-10,10)
	
def make_randlists(x, length=10):
	for i in range(0, x):
		yield list(make_randints(length))
	
class test_custom_sort_list(unittest.TestCase):
		
	def setUp(self):
		self.data = [custom_sort_list(i) for i in list(make_randlists(10))]

	def test_bubble(self):
		arr = self.data[:]
		sorted_arr = [sorted(i) for i in arr]
		[i.sort(algo='bubble') for i in arr]
		self.assertEqual(arr, sorted_arr)	
	
	def test_insertion(self):
		arr = self.data[:]
		sorted_arr = [sorted(i) for i in arr]
		[i.sort(algo='insertion') for i in arr]
		self.assertEqual(arr, sorted_arr)	

	def test_selection(self):
		arr = self.data[:]
		sorted_arr = [sorted(i) for i in arr]
		[i.sort(algo='selection') for i in arr]
		self.assertEqual(arr, sorted_arr)	

	def test_merge(self):
		arr = self.data[:]
		sorted_arr = [sorted(i) for i in arr]
		[i.sort(algo='merge') for i in arr]
		self.assertEqual(arr, sorted_arr)	

	def test_quick(self):
		arr = self.data[:]
		sorted_arr = [sorted(i) for i in arr]
		[i.sort(algo='quick') for i in arr]
		self.assertEqual(arr, sorted_arr)	

if __name__=='__main__':
	unittest.main()
