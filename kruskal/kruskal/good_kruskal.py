

def good_kruskal(arcs, number_of_nodes, parents = [], result = []):
	
	cost = 0

	numbers = []
	old = []

	arcs.sort()
	
	for i in xrange(number_of_nodes):
		parents.append(-1)
		result.append(-1)
		numbers.append(i)
		old.append(0)


	

	for arc in arcs:
		first_parent = find(arc[1], parents)
		second_parent = find(arc[2], parents)

		#print 'parent of',arc[1],'is', first_parent
		#print 'parent of', arc[2], 'is', second_parent
		
		if first_parent != second_parent and old[arc[2]]==0:
			union(first_parent,arc[2], parents)
			union(arc[1],arc[2],result)
			old[arc[2]] =1

	#print numbers
	print parents
	print result

def find(node, parents):
	while(parents[node] != -1):
		node = parents[node]
	return node

def union(first, second, parents):
	parents[second] = first


if __name__ == '__main__':
	good_kruskal()