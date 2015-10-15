a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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


	def printTree(self,root):
		if root:
			self.printTree(root.left)
			print root
			self.printTree(root.right)


if __name__ == "__main__":
	root = functions().createTree(a)
	# functions().printTree(root)
	print functions().exportToJson(root)