from typing import Dict, List, Optional

def inorder(root) -> List[int]:
	res = []
	curr = root
	while curr:
		if not curr.left:
			res.append(curr.val)
			curr = curr.right
			continue
		pre = curr.left
		while pre.right and pre.right is not curr:
			pre = pre.right
		if not pre.right:
			pre.right = curr
			curr = curr.left
			continue
		pre.right = None
		res.append(curr.val)
		curr = curr.right
	return res

def preorder(root) -> List[int]:
	res = []
	curr = root
	while curr:
		if not curr.left:
			res.append(curr.val)
			curr = curr.right
			continue
		pre = curr.left
		while pre.right and pre.right is not curr:
			pre = pre.right
		if not pre.right:
			pre.right = curr
			res.append(curr.val)
			curr = curr.left
			continue
		pre.right = None
		curr = curr.right
	return res

def postorder(root) -> List[int]:
	dummynode = TreeNode(-1)
	node = dummynode
	node.left = root
	res = []

	while node:
		if not node.left:
			node = node.right
			continue
		pre = node.left
		while pre.right and pre.right is not node:
			pre = pre.right
		if not pre.right:
			pre.right = node
			node = node.left
			continue
		pre = node.left
		par = []
		while pre.right and pre.right is not node:
			par.append(pre.val)
			pre = pre.right
		par.append(pre.val)
		res.extend(reversed(par))
		node = node.right

	return res

def postorder2(root) -> List[int]:
	dummynode = TreeNode(-1)
	node = dummynode
	node.left = root
	res = []

	while node:
		if not node.left:
			node = node.right
			continue
		pre = node.left
		while pre.right and pre.right is not node:
			pre = pre.right
		if not pre.right:
			pre.right = node
			node = node.left
			continue

		"""
		# same idea, easier to follow but O(n) in space
		pre = node.left
		par = []
		while pre.right and pre.right is not node:
			par.append(pre.val)
			pre = pre.right
		par.append(pre.val)
		res.extend(reversed(par))
		node = node.right
		"""

		prev = None
		curr = node.left
		next = curr.right

		while curr is not node:
			curr.right = prev
			prev = curr
			curr = next
			next = curr.right

		while prev:
			res.append(prev.val)
			prev = prev.right

		node = node.right

	return res

class TreeNode:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return f"{self.val}"

def decode(s: str) -> Optional[TreeNode]:
	if not s:
		return None

	s = tuple(map(int, s.split(",")))
	nodes: Dict[int, TreeNode] = {}
	n = len(s)
	i = 0
	while 2*i+1 < n:
		if s[i] not in nodes:
			nodes[s[i]] = TreeNode(s[i])
		if s[2*i+1] not in nodes:
			nodes[s[2*i+1]] = TreeNode(s[2*i+1])
		if 2*i+2 < n and s[2*i+2] not in nodes:
			nodes[s[2*i+2]] = TreeNode(s[2*i+2])

		nodes[s[i]].left = nodes[s[2*i+1]]
		if 2*i+2 < n:
			nodes[s[i]].right = nodes[s[2*i+2]]
		i += 1
	return nodes[s[0]]

root = TreeNode(1, TreeNode(2), TreeNode(3))
assert inorder(root) == [2,1,3]
assert inorder(decode("1,2,3,4,5,6,7")) == [4,2,5,1,6,3,7]

root = TreeNode(1, TreeNode(2), TreeNode(3))
assert preorder(root) == [1,2,3]
assert preorder(decode("1,2,3,4,5,6,7")) == [1,2,4,5,3,6,7]

root = TreeNode(1, TreeNode(2), TreeNode(3))
assert postorder(root) == [2,3,1]
assert postorder(decode("1,2,3,4,5,6,7")) == [4,5,2,6,7,3,1]

root = TreeNode(1, TreeNode(2), TreeNode(3))
assert postorder2(root) == [2,3,1]
assert postorder2(decode("1,2,3,4,5,6,7")) == [4,5,2,6,7,3,1]

print("\033[32mOK: checkout the code for the asserts\033[m")
