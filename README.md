# Morris algorithm in Python

https://en.wikipedia.org/wiki/Threaded_binary_tree

They're algorithms to explore a binary tree without recursion.

All these algorithms move down the tree like a fractal,
right to left, from bigger to smaller.

In inorder, you print the root when you're going back smaller
to bigger (meaning you already explored stuff on the left).

In preorder, you print the root when you're going
bigger to smaller (before exploring stuff on the left).

In postorder, you print _the diagonals in reverse order_
when going smaller to bigger.
