class node:
	def __init__(self,value,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

	def __setitem__(self,index,value):
		self[index] = value

	def __getitem__(self,index):
		return self[index]

	def __str__(self):
		return str(self.value)


class functions:

	def isBalanced(self,root):
		if root == None:
			return 0

		hl = self.isBalanced(root.left)
		hr = self.isBalanced(root.right)

		if hl == -1 or hr == -1:
			return -1

		if (hl-hr) > 1:
			return -1

		return max(hl+1,hr+1)

	def createFromJson(self,jsonTree):
		root = node(jsonTree["value"])

		if jsonTree["left"] == None:
			root.left = None
		elif type(jsonTree["left"]) == dict:
			root.left = self.createFromJson(jsonTree["left"])
		else:
			root.left = node(jsonTree["left"])

		if jsonTree["right"] == None:
			root.right = None
		elif type(jsonTree["right"]) == dict:
			root.right = self.createFromJson(jsonTree["right"])
		else:
			root.right = node(jsonTree["right"])

		return root

	def exportToJson(self,tree):
		root = {"value": tree.value}

		if tree.left == None:
			root["left"] = {}
		else:
			root["left"] = self.exportToJson(tree.left)

		if tree.right == None:
			root["right"] = {}
		else:
			root["right"] = self.exportToJson(tree.right)

		return root

	def createTree(self,array):
		if len(array) == 1:
			return node(array[0])

		lower_median = len(array)//2

		current_node = node(array[lower_median])

		if len(array[:lower_median]) > 0:
			current_node.left = self.createTree(array[:lower_median])

		if len(array[lower_median+1:]) > 0:
			current_node.right = self.createTree(array[lower_median+1:])

		return current_node

	def find(self,root,value):

		if not root:
			return None

		if root.value == value:
			return root

		returnValue = None

		if root.value > value:
			returnValue = self.find(root.left,value)
		else:
			returnValue = self.find(root.right,value)

		return returnValue



	def printTree(self,root):
		a = []

		if root:
			a.append(root.value)

			if root.left or root.right:
				a.append(self.printTree(root.left))
			if root.right:
				a.append(self.printTree(root.right))

		return a

	def checkIsBinarySearchTree(self,root,min=None,max=None):
		if not root:
			return True

		if(min and root.value < min) or (max and root.value > max):
			return False

		if self.checkIsBinarySearchTree(root.left,min,root.value) == False or self.checkIsBinarySearchTree(root.right,root.value,max) == False:
			return False

		return True

	# Fails with a = [1, 2, 3, 4, 50, 6, 7, 8, 9, 10]
	def checkIsBinarySearchTree_old(self,root):
		if not root:
			return True

		if root.left and root.left.value > root.value:
			return False

		if root.right and root.right.value < root.value:
			return False

		if self.checkIsBinarySearchTree(root.left) == False or self.checkIsBinarySearchTree(root.right) == False:
			return False

		return True

	def isEqual(self,rootA,rootB):

		if not rootA and not rootB:
			return True

		if rootA.value != rootB.value:
			return False

		return self.isEqual(rootA.left,rootB.left) and self.isEqual(rootA.right,rootB.right)

	def A_contains_B(self,rootA,rootB):

		if not rootB:
			return True

		rootA_ = self.find(rootA,rootB.value)

		return self.isEqual(rootA_,rootB)


	def fpv(self,root,value):

		result = self.findPathToValue(root,value)

		if len(result) > 0:
			return result

		result = self.findPathToValue(root.left,value)

		if len(result) > 0:
			return result

		result = self.findPathToValue(root.right,value)

		if len(result) > 0:
			return result

		return []

	def findPathToValue(self,root,value,path=[],valueSoFar=0):

		if not root:
			if valueSoFar == value:
				return path

			return []

		if root.value == value:
			return [root.value]

		valueSoFar += root.value

		result = self.findPathToValue(root.left,value,path+[root.value],valueSoFar)

		if len(result) > 0:
			return result

		result = self.findPathToValue(root.right,value,path+[root.value],valueSoFar)

		if len(result) > 0:
			return result

		if valueSoFar == value:
			return path+[root.value]

		return []


if __name__ == "__main__":
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# b = [2, 3, -4, 4, -2, 6, 7, 8, 6, 10, 11, 12 ,13,14,15,16,17]

	# a = [1, 2, 3, 4, 5, 6]
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


	rootb = functions().createTree(b)
	# roota = functions().createTree(a)
	# print functions().A_contains_B(roota,rootb)
	# http://mshang.ca/syntree/
	print str(functions().printTree(rootb)).replace(",","")
	# print functions().exportToJson(root)
	# print functions().checkIsBinarySearchTree(root)
	# print str(functions().printTree(rootb)).replace(",","")
	print functions().fpv(rootb,15)