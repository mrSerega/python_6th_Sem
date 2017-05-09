class Heap(object):
	
	A = []
	size = 0

	def __init__(self, A):
		self.A = A;
		self.size = len(A)
		self.heapify()

	def repair_o(self, index):
		k = index
		#print (self.size-1) // 2
		while k <= ((self.size-1) // 2):
			k1 = 2*k + 1
			k2 = k1 + 1
			if k2 < self.size and self.A[k2] < self.A[k1]:
				k1 = k2
			if self.A[k] < self.A[k1]:
				break
			else:
				self.A[k], self.A[k1] = self.A[k1], self.A[k]
			k = k1

	def repair_i(self, index):
		k = index		
		while k > 0:
			k1 = (k-1) // 2
			if self.A[k1] < self.A[k]:
				break
			self.A[k], self.A[k1] = self.A[k1], self.A[k]
			k = k1

	def pop_min(self):
		min = self.A[0]
		self.A[0] = self.A[self.size-1]
		self.size -=1
		self.repair_o(0)
		return min

	def add(self, value):
		try:
			self.A[self.size] = value
		except:
			self.A.append(value)
		self.size +=1
		self.repair_i(self.size-1)

	def remove(self,index):
		a = self.A[index]
		self.A[index] = self.A[self.size-1]
		self.size -=1
		if self.A[index] > a:
			self.repair_o(index)
		else:
			self.repair_i(index)

	def heapify(self):
		k = (self.size-1) // 2
		while k >= 0:
			#print k
			self.repair_o(k)
			#print self.A
			k-=1

def test():
	A = [8,7,6,5,4,3,2,1]
	heap = Heap(A)
	while heap.size > 0:	
		#print heap.A
		print heap.pop_min()
	heap.add(3)
	heap.add(7)
	heap.add(0)
	heap.remove(1)
	#print heap.A
	print heap.pop_min()	
	print heap.pop_min()

if __name__ =='__main__':
	test()