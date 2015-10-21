a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import tree as t

# class node:
# 	def __init__(self,value,left=None,right=None):
# 		self.value = value
# 		self.left = left
# 		self.right = right

# 	def get_left(self):
# 		return self.left

# 	def set_left(self,left):
# 		self.left = left

# 	def get_right(self):
# 		return self.right

# 	def set_right(self,right):
# 		self.right = right

class linkedListItem:

	def __init__(self,value,next=None):
		self.value = value
		self.next = next
		self.last = self

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next

	def get_value(self):
		return self.value

	def insert(self,value):
		newItem = linkedListItem(value)
		self.last.set_next(newItem)
		self.last = newItem




def createLinkedList(tree,depth=1,linkedListArray=[]):

	if len(linkedListArray) >= depth:
		linkedListArray[depth-1].insert(tree.value)
	else:
		linkedListArray.append(linkedListItem(tree.value))

	if tree.left:
		createLinkedList(tree.left,depth+1,linkedListArray)

	if tree.right:
		createLinkedList(tree.right,depth+1,linkedListArray)

	return linkedListArray

for i in  createLinkedList(t.functions().createTree(a)):
	a = []
	a.append(i.get_value())
	j = i.get_next()
	while j:
		a.append(j.get_value())
		j = j.get_next()
	print a