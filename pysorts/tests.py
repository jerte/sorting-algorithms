import unittest
from random import randint
from bubble import bubble_sort
from insertion import insertion_sort
from selection import selection_sort
from merge import merge_sort, merge

def make_randomints():
	data = []	
	for i in range(0, 20):
		case = []
		case_length = randint(2,10)
		for j in range(0, case_length):
			case.append(randint(-10,10))
		data.append(case)
	return data

class test_sorts(unittest.TestCase):

	def test_bubble(self):
		data = make_randomints()	
		sorted_data = [sorted(i) for i in data]
		self.assertEqual([bubble_sort(i, min) for i in data], sorted_data)
	
	def test_insertion(self):
		data = make_randomints()	
		sorted_data = [sorted(i) for i in data]
		self.assertEqual([insertion_sort(i, min) for i in data], sorted_data)
	
	def test_selection(self):
		data = make_randomints()	
		sorted_data = [sorted(i) for i in data]
		self.assertEqual([selection_sort(i, min) for i in data], sorted_data)
	
	def test_merge(self):
		data = make_randomints()	
		sorted_data = [sorted(i) for i in data]
		for i in data:
			merge_sort(i, min, 0, len(i))
		self.assertEqual(data, sorted_data)

if __name__=='__main__':
	unittest.main()
