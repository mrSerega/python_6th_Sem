import ArcList

class Buckets(object):
	
	buckets = []

	def __init__(self, buckets_number):
		for bucket in xrange(buckets_number):
			self.buckets.append([])

	def insert(self, node_index, bucket_index):
		self.buckets[bucket_index].append(node_index)

	def remove(self, node_index, bucket_index):
		self.buckets[bucket_index].remove(node_index)

	def pop(self, bucket_index):
		if len(self.buckets[bucket_index]) == 0:
			return -1
		return self.buckets[bucket_index].pop()

	def size(self):
		return len(self.buckets)

class Graph(object):
	
	num_of_nodes = 0
	max_arc_cost = 0

	arclist = None

	def __init__(self, graph_size, cost, left, right ):
		self.num_of_nodes = graph_size
		self.max_arc_cost = max(cost)
		self.arclist = ArcList.Arclist(graph_size,  cost, left, right)

	def size(self):
		return self.num_of_nodes

	def max_arc_value(self):
		return self.max_arc_cost

	def get_out_arcs(self, index):
		arcs = []
		i = self.arclist.H[index]
		while(i != -1):
			arcs.append(Arc(self.arclist.C[i], self.arclist.I[i], self.arclist.J[i]))
			i = self.arclist.L[i]
		return arcs

class Arc(object):

	__left = 0
	__right = 0
	__cost = 0

	def __init__(self, cost, left, right):
		self.__left = left
		self.__right = right
		self.__cost = cost
	
	def right(self):
		return self.__right

	def left(self):
		return self.__left

	def cost(self):
		return self.__cost

def Dijkstra(graph, start_node_index):
	distances = []
	
	for i in xrange(graph.size()):
		distances.append(float('inf'))

	parents = []

	for i in xrange(graph.size()):
		parents.append(-2)

	distances[start_node_index] = 0
	parents[start_node_index] = -1

	buckets_max_number = graph.size()*graph.max_arc_value()
	
	buckets = Buckets(buckets_max_number)

	buckets.insert(start_node_index, 0)

	for bucket in xrange(buckets.size()):
		node = None
		while(node != -1):
			node = buckets.pop(bucket)
			for arc in graph.get_out_arcs(node):
				distance = distances[arc.right()]
				if distances[arc.left()]+arc.cost() < distance:
					distances[arc.right()] = distances[arc.left()]+arc.cost()
					parents[arc.right()] = arc.left()
					if distance != float('inf'):
						buckets.remove(arc.right(), distance)
					buckets.insert(arc.right(), distances[arc.right()])
	
	return distances, parents
	
def main():
	_cost=[]
	_left=[]
	_right=[]
	_cost.append(1); _left.append(0); _right.append(4)
	_cost.append(2); _left.append(0); _right.append(1)
	_cost.append(2); _left.append(0); _right.append(3)
	_cost.append(2); _left.append(1); _right.append(0)
	_cost.append(2); _left.append(1); _right.append(3)
	_cost.append(1); _left.append(1); _right.append(4)
	_cost.append(2); _left.append(2); _right.append(1)
	_cost.append(2); _left.append(2); _right.append(3)
	_cost.append(1); _left.append(2); _right.append(4)
	_cost.append(2); _left.append(3); _right.append(2)
	_cost.append(1); _left.append(3); _right.append(4)
	_cost.append(2); _left.append(3); _right.append(0)
	_cost.append(1); _left.append(4); _right.append(0)
	_cost.append(1); _left.append(4); _right.append(1)
	_cost.append(1); _left.append(4); _right.append(2)
	_cost.append(1); _left.append(4); _right.append(3)
	
	graph = Graph(5,_cost,_left,_right)
	trees = []
	parents = []
	for i in xrange(graph.size()):
		tree, parent = Dijkstra(graph, i)
		trees.append(tree)
		parents.append(parent)

	min_sum = float('inf')
	min_index = 0
	index = 0
	for tree in trees:
		sum_value = sum(tree)
		if sum_value < min_sum:
			min_index = index
			min_sum = sum_value
		index +=1

	print trees
	print min_index
	print trees[min_index] 
	print parents[min_index]

if __name__ == '__main__':
	main()