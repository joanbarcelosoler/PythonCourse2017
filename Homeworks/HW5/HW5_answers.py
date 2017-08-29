class Node:
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next
		self.prev = None
	
	def __str__(self):
		return str(self.value)
	
	def first(self):
		return self.value
	
	def rest(self):
		return self.next
	
	def set_first(self, _value):
		self.value = _value
	
	def set_rest(self, _value):
		self.next = _value

class LinkedList:
	def __init__(self, head=None):
		self.head = None
		self.tail = None
		self.node = None
		self.length = 0
	
	def length(self):
		return self.length
	
	def addNode(self, new_value):
		if type(new_value) == int:
			new_node = Node(new_value)
			if self.head == None: # if the list is empty
				self.head = new_node 
				self.tail = new_node
				self.length += 1
			elif self.head.next == None: # if the list has just one item
				self.node = self.head
				self.node.next = new_node
				self.tail = self.node.next
				self.head.next = self.node.next
				self.tail.prev = self.node
				self.length += 1
			else: # if the list has more than two item
				self.node = self.tail
				self.node.next = new_node
				self.tail = self.node.next
				self.length += 1
		else:
			return "Only Integer!"
	
	def addNodeAfter(self, new_value, after_node):
		if type(new_value) == int and type(after_node) == int:
			if after_node <= self.length: # if the node is within the range
				if self.head == None: # if the list is empty
					self.head = Node(new_value) 
					self.tail = new_node
					self.length += 1
				else: # if inserting to other locations
					self.node = self.head
					for i in range(after_node): # loop and go the the location after which a new node is inserted
						self.node = self.node.next
						i += 1
					next_of_next = self.node.next
					self.node.next = Node(new_value)
					self.node.next.prev = self.node
					self.node = self.node.next
					self.node.next = next_of_next
					self.length += 1
			else:
				return "Out of Range!"
		else:
			return "Only Integer!"
	
	def addNodeBefore(self, new_value, before_node):
		if type(new_value) == int and type(before_node) == int:
			if before_node <= self.length: # if the node is within the range
				if before_node == 0 or not self.head: # if inserting before the head or the list is empty
					self.head = Node(new_value, self.head)
					self.length += 1
				else: # if inserting to other locations
					cp = self.head
					while cp.rest(): # iterate each node until before_node-1 bocomes 0
						before_node -= 1
						if before_node == 0:
							break
						cp = cp.rest()
					new_cp = Node(new_value, cp.rest()) # create new_node here
					cp.set_rest(new_cp) # connect new_node with the rest of the list
					self.length += 1
			else:
				return "Out of Range!"
		else:
			return "Only Integer!"
	
	def removeNode(self, node_to_remove):
		if type(node_to_remove) == int:
			if node_to_remove <= self.length: # if the node is within the range
				if node_to_remove == 0: # if removing the head
					self.head = self.head.rest() # the new head is the next to the old head
					self.length -= 1
				else:
					cp = self.head
					while cp.rest():
						node_to_remove -= 1 # iterate each node until node_to_remove-1 becomes 0
						if node_to_remove == 0:
							cp.set_rest(cp.rest().rest()) # remove the node and connect cp and cp.rest.rest
						cp = cp.rest()
					self.length -= 1
			else:
				return "Out of Range!"
		else:
			return "Only Integer!"
	
	def removeNodesByValue(self, value):
		previous = None
		cp = self.head
		while cp != None: # loop through the nodes
			if cp.value == value: # if it is the one we want to remove
				if cp == self.head:
					self.head = self.head.next
				else:
					previous.next = cp.next
			else:
				previous = cp
			cp = cp.next
	
	def reverse(self): # Honestly, this answer is based on online information, I am not sure whether it actually works...
		import copy
		mirror = copy.deepcopy(self)
		mirror.node = mirror.head
		self.node = self.tail
		while self.node != None:
			mirror.node.value = copy.deepcopy(self.node.value)
			mirror.node = mirror.node.next
			self.node = self.node.prev
		self.node = self.head
		mirror.node = mirror.head
		while self.node != None:
			self.node.value = copy.deepcopy(self.node.value)
			mirror.node = self.node.next
			mirror.node = mirror.node.next
			
	def __str__(self):
		cp = self.head
		while cp != None:
			print(cp.value)
			cp = cp.next

		

list = LinkedList()
list.addNode(1) #[1]
list.addNode(2) #[1,2]
list.addNode(3) #[1,2,3]
list.addNode(4) #[1,2,3,4]
list.addNode(1) #[1,2,3,4,1]
list.addNode(1) #[1,2,3,4,1,1]
list.addNodeAfter(5, 3) #[1,2,3,4,5,1,1]
list.addNodeAfter(6, 2) #[1,2,3,6,4,5,1,1]
list.addNodeBefore(7, 0) #[7,1,2,3,6,4,5]
list.addNodeBefore(8, 2) #[7,1,8,2,3,6,4,5,1,1]
list.removeNode(2) #[7,1,2,3,6,4,5,1,1]
list.removeNodesByValue(1) #[7,2,3,6,4,5]
list.reverse()
link.__str__()
list.length
