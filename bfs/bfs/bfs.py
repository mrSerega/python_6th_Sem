import ArcList
import readGraph

def bfs(start_node_index, graph):
	distance = []
	parents = []

	for i in xrange(graph.size()):
		distance.append(graph.size())
		parents.append(-2)

	distance[start_node_index] = 0
	parents[start_node_index] = -1

	queue = []
	queue.append(start_node_index)

	r = 0
	w = 1

	while r < w:
		i = queue[r]
		r += 1
		k = graph.H[i]
		while k != -1:
			j = graph.J[k]
			if distance[j] == graph.size():
				distance[j] = distance[i] + 1
				parents[j] = k
				queue.append(j)
				w += 1
			k = graph.L[k]
	return distance, parents

def main():
	distance, parents = bfs(0,readGraph.readg('input.txt'))
	print parents
	print distance

if __name__ == '__main__':
	main()