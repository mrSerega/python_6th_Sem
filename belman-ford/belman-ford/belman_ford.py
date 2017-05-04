import ArcList
import readGraph

def bf(start_node_index, graph):

	#list init
	sizes = []
	queue = []	
	parents = []

	#size init
	for node in xrange(graph.size()):
		sizes.append(float('inf'))

	#parents init
	for node in xrange(graph.size()):
		parents.append(-2)

	#start node init
	sizes[start_node_index] = 0
	parents[start_node_index] = -1

	#queue init
	for node in xrange(graph.size()):
		queue.append(-2)
	queue_head = start_node_index
	queue_tail = start_node_index
	queue[start_node_index] = -1

	#do the deal
	while queue_head != -1:
		i = queue_head
		
		queue_head = queue[queue_head]
		queue[i] = -2

		arc = graph.H[i]
		while arc != -1:
			j = graph.J[arc]
			rj = sizes[j]
			if sizes[i] + graph.C[arc] < rj:
				sizes[j] = sizes[i] + graph.C[arc]
				parents[j] = arc
				if queue[j] == -2:
					if queue_head != -1:
						queue[queue_tail] = j
					else:
						queue_head = j 
					queue_tail = j
					queue[j] = -1
			arc = graph.L[arc]

	return sizes, parents

def main():
	size, parent = bf(0,readGraph.readg('input.txt'))
	print parent
	print size
	
if __name__ == '__main__':
	main()