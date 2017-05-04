class Arclist:

	I = [] #arc start
	J = [] #arc end
	H = [] #heads
	L = [] #links
	C = [] #cost
	free = []

	count = 0

	def __init__(self, num, c_list, i_list, j_list):
		self.set_num_of_nodes(num)
		for i in range(len(i_list)):
			self.add_edge(i_list[i],j_list[i], c_list[i])

	def set_num_of_nodes(self, num):
		for i in range(num):
			self.H.append(-1)

	def add_edge(self, left, right, cost):
		if len(self.free) == 0:
			self.I.append(left)
			self.J.append(right)
			self.C.append(cost)
			self.L.append(self.H[left])
			self.H[left]=len(self.L)-1
		else:
			self.I[free[0]]=left
			self.J[free[0]]=right
			self.C[free[0]]=cost
			self.L[free[0]]=self.H[left]
			self.H[left]=self.free[0]
			self.free.pop(0)

	def remove_edge(self, index):
		self.free.append(index)
		it_left = self.H[self.I[index]]
		it_right = self.H[self.J[index]]
		if it_left == index: 
			self.H[it_left] = self.L[self.H[it_left]]
		else:
			while(self.L[it_left]!=index):
				it_left = self.L[it_left]
				if it_left == -1: return
			self.L[it_left] = self.L[self.L[it_left]] 
		if it_right == index: 
			self.H[it_right] = self.L[self.H[it_right]]
		else:
			while(self.L[it_right]!=index):
				it_right = self.L[it_right]
				if it_right == -1: return
			self.L[it_right] = self.L[self.L[it_right]] 

	def print_lists(self):
		print(self.I)
		print(self.J)
		print(self.H)
		print(self.L)

	def make_norm_graph(self, G):
		G.clear()
		for i in range(len(self.H)):
			G.add_node(i)
			it = self.H[i]
			while(it!=-1):
				G.add_edge(self.I[it],self.J[it])
				it = self.L[it]
