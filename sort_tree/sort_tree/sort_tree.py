import heap

def sort_tree(list_to_sort):
	h = heap.Heap(list_to_sort)
	ret = []
	while h.size > 0:
		ret.append(h.pop_min())
	return ret

def test():
	list_to_sort = [30,1,3,4,7,6,12,11,-5,-6,-2]
	list_to_sort = sort_tree(list_to_sort)
	print list_to_sort

if __name__ == '__main__':
	test()