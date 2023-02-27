import patient as p
class MaxHeap:

	def __init__(self):
		self.maxsize = 200
		self.size = 0
		self.Heap = [None] * (self.maxsize + 1)
		self.Arr = []
		self.FRONT = 1
		self.arr_size = 0

	# Function to return the position of
	# parent for the node currently
	# at pos
	def parent(self, pos):
		return pos // 2

	# Function to return the position of
	# the left child for the node currently
	# at pos
	def leftChild(self, pos):
		return 2 * pos

	# Function to return the position of
	# the right child for the node currently
	# at pos
	def rightChild(self, pos):
		
		return (2 * pos) + 1

	# Function that returns true if the passed
	# node is a leaf node
	def isLeaf(self, pos):
		
		if pos > (self.size//2) and pos <= self.size:
			return True
		return False

	# Function to swap two nodes of the heap
	def swap(self, fpos, spos):
		# print("Swap: {} {}".format(self.Heap[fpos].age, self.Heap[spos].age))
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

	# Function to heapify the node at pos
	def maxHeapify(self, pos):
		# print("{} {}".format(pos, self.Heap[pos].age))
		# print(self.isLeaf(pos))
		if not self.isLeaf(pos):
			# print("f")
			# print(self.Heap[self.leftChild(pos)] != None)
			# print(self.Heap[self.leftChild(pos)].age)
			# print(self.Heap[pos].age < self.Heap[self.leftChild(pos)].age)
			# print(self.Heap[self.leftChild(pos)] != None and self.Heap[pos].age < self.Heap[self.leftChild(pos)].age)
			if ((self.Heap[self.leftChild(pos)] != None and self.Heap[pos].age < self.Heap[self.leftChild(pos)].age) or (self.Heap[self.rightChild(pos)] != None and self.Heap[pos].age < self.Heap[self.rightChild(pos)].age)):
				# print("m")
				# Swap with the left child and heapify
				# the left child
				if (self.Heap[self.rightChild(pos)] != None and (self.Heap[self.leftChild(pos)].age > self.Heap[self.rightChild(pos)].age)):
					# print("a")
					self.swap(pos, self.leftChild(pos))
					self.maxHeapify(self.leftChild(pos))
				elif (self.Heap[self.rightChild(pos)] == None):
					# print("b")
					self.swap(pos, self.leftChild(pos))
					self.maxHeapify(self.leftChild(pos))
				# Swap with the right child and heapify
				# the right child
				else:
					# print("c")
					self.swap(pos, self.rightChild(pos))
					self.maxHeapify(self.rightChild(pos))

	# Function to insert a node into the heap
	def insert(self, element):
		if self.size >= self.maxsize:
			return
		self.Arr.append(element)
		self.size += 1
		self.Heap[self.size] = element

		current = self.size

		while (self.Heap[current] != None and self.Heap[self.parent(current)] != None and self.Heap[current].age > self.Heap[self.parent(current)].age):
			self.swap(current, self.parent(current))
			current = self.parent(current)

	# Function to remove and return the maximum
	# element from the heap
	def getTop(self):
		if self.size == 0:
			return -1, -1
		if self.Heap[self.FRONT] == None:
			return -1, -1
		name = self.Heap[self.FRONT].name
		id = self.Heap[self.FRONT].id
		self.Arr.remove(self.Heap[self.FRONT])
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.Heap[self.size] = None
		# print(self.size)
		self.size -= 1
		# print(self.size)
		# print(self.Heap[self.FRONT].age)
		# print("++")
		self.maxHeapify(self.FRONT)
		# print(self.Heap[self.FRONT])
		return name, id
	
	def showQueue(self):
		self.Arr.sort(key=lambda x:x.age, reverse=True)
		for i in range(0, len(self.Arr)):
			print("{} {}".format(i+1, self.Arr[i].name))

	def showHeap(self):
		print("Data in the heap is as follows:")
		for i in range(1, (self.size // 2) + 1):
			print("Parent: {}" .format(self.Heap[i].name))
			if self.Heap[self.leftChild(i)] != None:
				print("Left: {}" .format(self.Heap[self.leftChild(i)].name))
			if self.Heap[self.rightChild(i)] != None:
				print("Right: {}".format(self.Heap[self.rightChild(i)].name))
	        
