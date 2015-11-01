################################################
# Explanation on http://neymello.me/?p=8
################################################


class node:
	# Initiate an instance of Node
	def __init__(self,value,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

	def __setitem__(self,index,value):
		self[index] = value

	def __getitem__(self,index):
		return self[index]

	# Print the instance's value
	def __str__(self):
		return str(self.value)


def isBalanced(self,root):
	# Check if root is null
	if root == None:
		return 0

	# Calculate the depth of the left subtree (recursively)
	depthLeft = self.isBalanced(root.left)

	# Calculate the depth of the right subtree (recursively)
	depthRight = self.isBalanced(root.right)

	# Return is -1 (not balanced) if -1 if found in some place
	# during the call
	if depthLeft == -1 or depthRight == -1:
		return -1

	# If the difference is greater than 1, return -1
	if (depthLeft-depthRight) > 1:
		return -1

	# Otherwise return the max depth
	return max(depthLeft+1,depthRight+1)