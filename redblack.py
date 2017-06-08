# sorting the sorted array
# it become a linked list so the O(N) for binary search tree
# if we convert binary search tree to balanced tree time complexity changes to O(logN) for all operations

# running time of BST operations depends on the height of the binary search tree.
# balanced tree gives best performance
# in AVL heights of the two child subtrees of any node differ by at most one
# another solution is red-black trees
# AVL trees are faster than red-black trees because they are more rigidly balanced but needs more work
# OS rely on these data structures


# Red black properties
# 1. each node is either red or black
# 2. Root node is always black
# 3. all leaves NIL or NULL are black
# 4. every red node must have two black child nodes and no other children it must have black parent
# 5. each path from a given node to any of its descendant NIl/NULL nodes contains the same number of black nodes

# linux kernels relies heavily on red-black tree data strcuture
# Insertion is fast -> because it is not rigidly balanced and we do not bother about making the tree as balanced as possible
# For insert intensive tasks use a red-black tree
# Exampl: java.util.TreeMap, java.util.TreeSet
# C++ STL: map, multipmap, multiset

# use Red-Black Tree use for insert operations --> Search is slow
# AVL Tree good for lookup --> insert and delete operation is slow coz we need to rebalanced

