# BreadthFirstSearch is usually implemented with Queue
# DepthFirstSearch we could use stack but usuallly we implement it with recurssion. It is under the hood uses stack of the operating system.

class Node(object):

	def __init__(self, name):
		self.name = name
		self.adjacentList = []
		self.visited = False
		self.predecessor = None

class BreadthFirstSearch(object):

	def bfs(self, startNode):
		queue = []
		queue.append(startNode)
		startNode.visited = True

		while queue:

			actualNode = queue.pop(0)
			print ("%s " % actualNode.name)

			for n in actualNode.adjacentList:
				if not n.visited:
					n.visited = True
					queue.append(n)

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node1.adjacentList.append(node4)
node1.adjacentList.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)
