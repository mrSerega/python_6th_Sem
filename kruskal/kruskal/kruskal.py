def main():
	cost = 0
	result = []
	n = 7 #input here
	nodes = [(3,0,1),(1,0,2),(2,0,4),(7,0,5),(9,1,2),(2,2,3),(8,2,4),(4,3,4),(5,3,6),(5,4,5),(7,4,6),(4,5,6)] #input here
	m = len(nodes)
	tree_id = []
	nodes.sort()
	
	for i in xrange(n):
		try:
			tree_id[i] = i
		except:
			tree_id.append(i)

	for i in xrange(m):
		a = nodes[i][1]
		b = nodes[i][2]
		l = nodes[i][0]
		if tree_id[a] != tree_id[b]:
			cost += l
			result.append((a,b))
			old_id = tree_id[b]
			new_id = tree_id[a]
			for j in xrange(n):
				if tree_id[j] == old_id:
					tree_id[j] = new_id

	print result

if __name__ == '__main__':
    main()