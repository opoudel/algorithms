#Abstract Data Types & Data Structures
## Abstract Data Types
	+ Interfaces in Java
	+ Super Types
	+ Without a concrete implementation
	+ Just tells the behaviour

##Data Structure
	- Concrete implementation of ADTs
	- Best case scenario:
			O(1) time complexity to insert
			O(1) time compexity to retrieve Item

## Examples
Abstract Data Types | Data Structures
--- | ---
Stack | array, linked list
Queue | array, linked list
Priority Queue | heap
Dictionary & hashmap | array

#Complexity Theory Basics
- Space Complexity: how much memory an algorithm needs
- Time Complexity: how much time an algorithm needs ( as fast as possible)

##Time Complexity: 
	- Do not consider absolute time?
	- Consider number of steps 
	- Question you ask is how the algorithm running time depends on INPUT SIZE
	- How algorithm will scale and behave with the input size
	- We like deterministic algorithms where the running times are approximitaly linear

##Asymptotic analysis
 	- How algorithm is going to behave when we have to sort large input size

###Big O notation: Defines upper bound
	- It describes the limiting behavior of a function, when argument tends towards a particular value or infinity
	- function of running time
	- it is used to classify algorithms by how they respond to changes in input size

```
 		f(n) = O(g(n)) expression means that there is some c>0 value and some n >0 threashold such that n>nx the | f(n) | <= c* |g(n)|

		if we have an O(N^2) running time complexity, it is also true it is in O(N^3) or O(N^4) or O(N^5)
```

###Big Omega Notation: Defines lower bound
	- describes the limiting behavour of a function when argument tends towards a particular valur or infinity
	- Number Theory: it means that f(n) function is not dominated by g(n) function asymptotically
	- Complexity Theory: it means that an f(n) function is bounded below by an g(n) function asymptotically fn = Omega(g(n))
	- if we have an Omega(N^2) running time complexity, it is also true it is in Omega(N), Omega(logN) or Omega(1)

###Big Theta Notation:
	- when f(n) = O(g(n)) f(n) = Omega(g(n))
	- have upper and lower bownd



##Algorithms running time:
	1) Constant Time Complexity: O(1)
	2) Logarithmic Complexity: O(logN)
	3) Linear Time Complexity: O(N)
	4) Linearthmetic Complexity: O(N*logN)
	5) Polynomial Complexity: O(n^k)
	6) Exponential Complexity: O(c^n) C is constant
	7) Factorial Complexity: O(n!)

###Constant Time complexity: O(1)
	- Swapping two numbers or deciding whether a number is odd or even
	- Fastest algorithm
	- Random Access of array

###Logarithmic Time Complexity: O(logN): 
	- Finding an arbitary item in sorted array 
			-- (1, 2, 3, 4, 5 6, 7, 8, 9, 10) ==> 1,2,3,4,5 ==> 1, 2, 3 ==> 1, 2 ==> 1
	- Checking whether there is a cycle in a graph when solving Kruscal algorithm
	- Binary search

###Linear Time Complexity: O(N):
	- Finding the minimum or maximum value in the array of numbers
	- Iterating through all items is N
	- Linear search

###Linearthmetic Complexity O(N*logN)	
	- Mergesort
	- Quick sort
	- Heap sort
	- Finding closest pair of points with divide and conquer method

####Below are the slower Algorithms

###Polynomial Time Complexity O(N^k) 
	- When k = 2 it becomes O(N^2)
	- Bubble sort
	- Insertion sort
	- Finding closest pair of points with brute force approach

###Exponential Algorithms:
	- O(c^N)
	- Towers of hanoi problems
	- Calculate fibonacci numbers with recursive manner ~ c=2 here too
	- Travelling salesman problem with dynamic programming implementation

###Factorial Time Complexity
	- O(N!)
	- solving travelling salesman problem with brute force.
	- try to find one with minimum overall distance


#Complexity Classes:

##P complexity class;
	- Polynomial
	- Bubble sort can be solved by merge sort

##NP complexity class;
	- Non-deterministic Polynomial
	- Bubble sort can be solved by merge sort

##NP Complete complexity class;
	- Polynomial
	- Bubble sort can be solved by merge sort

##NP Hard

#Time complexity of different operations
##Loops
	- Function value assignment --> O(1) single operation
	- Single for loop and has only O(1) operations inside it such as print or finding value: O(N) time complexity
	- Nested For Loop: O(N^k) where k = number of for loops --> Quadratic running time

##Linear search:
	- Best case scenario, you get item in first index search. First element of array ==> O(1)
	- Worst case scenario, there is no element that you are searching for in an Array	==> O(N)

##Binary Search:
	- Divide array into halves for x number of times until there is one item left.
	- 1 = N/2^x
	- 2^x = N
	- log 2^x = log N
	- x = log N

##Bubble Search: O(N^2)
	- Quadratic time complexity

#Time complexity of Data Types

##Array
	- Advantages: Random Access, O(1)
	- Disadvantages: Compile time Sizing, Expanding array require O(N) operation, does not store differen types
	- Operations:
		- Append Operatoin - O(1)
		- Insert at the already occupied index: O(N) (including first item)
		- Remove Last item Operation - O(1)
		- Remove by index -O(N) because it will require reconstructing array 

###Arrays in Python:
	- Does not have native Array like above but have "list" general purpose array
	- List : ordered collection of items

##Linked List
	+ They are nodes and points to another node
	+ Last node points to null so we know it is last node
	+ Single Node:	
	+ Contains interger, double or custom object
	+ Contains a reference pointing to the next node in the linked list
	  
		```	  example:
			  	class Node {
			  		data
			  		Node nextNode
			  	}
		```
	+ Used to implement stacks and queues
	+ Simple linked list do not allow random access
	+ Many basic operations require visiting most or all items in the list O(N) except the first item in the linked list O(1)

###Advantages:
	+ they are dynamic data structures (Arrays are not)
	+ It can allocate memory during runtime O(1)
	+ very efficient when we want to manipulate the first element
  		+ 
###Disadvantages:
	+ waste of memory becuase of reference value
	+ Nodes in the linked list must be read in order from the beginning as linked list have sequential access, 
	+ difficult to navigate backward, so add preiovus item reference doubly linked lists
		
	+ Operations
		- Inserting items at the beginning of the linked list
			- O(1)
		- Insertint item at the end of the linked list require traversing entire list to find null
		- O(N)
			- updating reference of null is O(1) but overall operation is O(N)	so O(N) + O(1) = O(N) asymtotically
			- Removing item from the beginning is O(1)
			- Removing item from the end or any point is O(N)

	- Problems:
		- Simple Linked list reverse traversing is impossible
		- Doubly linked list works great

###Difference between linked list and Array	
	- Search
		- Search operation yields the same result for both data structure
		- ArrayList search operation is pretty faster compared to the linkedList search operation
		- getItem in array is O(1), but in linked list it is O(N)
	- Deletion
		- Linked List deletion is O(1) for the first item
		- Array List deletion is O(N) for the first item
		- Linked List inserting to end of list is O(N)
		- Array List inserting to end of list is O(1)
		- Array once find the element O(N) operation, delete record O(1) and reconstruct array O(N) operation
		- Linked List find the element O(N) operation, deletion O(1) and change pointer O(1)
		- Linked List is faster for Deletion

	- Memory Management	
		- array are better because of no references. linked list has space complexity O(N)

###Doubly Linked List:
	- pointer to both previous and next node
	- removal of a node is O(1) if we know the item.

##Stack: Abstract Data Type
	+ Interface
	+ Basis Operation pop(), push(), peek()
	+ LIFO operation
	+ Operations:
		+ Push --> O(1) adding item to the top of the stack
		+ Pop --> O(1) removing item the one added last, 
		+ Peek --> O(1) return item without removing from the stack
	+ Usage in Graphs

###Stack Memory:
	+ It is a specialy memory in RAM
	+ it keeps track of the point to which each active subroutine should return control when it finishes executing
	+ Stores temporary variables created by each function
	+ Local variables are in stack
	+ Stack memory is limited

###Heap Memory:
	+ Not managed automatically for you. It is in RAM
	+ C: malloc(), calloc()
	+ Java: reference types and object at the heap
	+ we have to dellocate to remove it from heap -- garbage collection

###Stack and Recursion:
	+ Recursion uses stacks by OS
	+ 

##Queue: Abstract data type
	+ Basic operations
		+ enqueue
		+ dequeue
		+ peek()
	+ FIFO structure
	+ Can be implemented with dynamic array as well as linked list
	+ important for BFS graph algorithms
	+ Usage:
		+ shared resources 
		+ I/O buffers
		+ CPU Scheduling
		+ data transferred asynchronously
	+ Breadfort search, big search
	+ Priority Queue for graph traversal

##Binary Search Tree: (data structure)
	- Sorted Array
		- inserting new item slow O(N)
		- Searching is fast O(logN)
		- Removing item is slow O(N)
	- Linked List:
		- inserting new item fast O(1)
		- searching is seuqnetial O(N)
		- removing item is fast O(1)

##Binary Trees****:
	+ From one node to another there is only one path			
	+ Parent/Child link
	+ can have more than 2 childs

##Binary Search Tree:
	+ Can only have 2 childs at max
	+ left child is smaller than parent
	+ right child is greater than parent
	+ Height of the tree - layers of the tree
	+ Height of the tree h = log n
	+ Balanced Tree: Number of left child = number of right

	+ Operations:
		+ insert/search operation is O(logN)
		+ delete:
			+ soft delete: not efficient
			+ three possible cases
				+ delete leaf node
				+ delete node with one single child
				+ delete node with two child
					+ largest item in the left subtree (Predessor)
					+ or find smallest item in the right hand side (Successor)
		+ Traversal
			+ In order traversal: left subtree + root node + right sub tree recursively, gives numerical or alpahbetica ordering (normally used)
			+ Pre Order traversal: root --> left --> right recursively
			+ Post order traversal: left subtree -> right --> root recursively
	+ Building binary search tree from the sorted array is worst because it will have right childs only and traversal is like linked list O(N)
	+ Binary tree must be as balanced as possible


##Balanced Binary Trees: 
	+ if height of the tree is either greater than 1 or less than -1 then it will be unbalanced.
		+ AVL
		+ Red-Black trees
	Problems:
		- sorted array [1,2,3,4] result into linked list so the operation is O(N) ****BAD****
	- AVL Trees:
		- tree balanced and best performance
		- height of the two child subtrees of any node differ by at most one
		- AVL Trees are faster than Red-Black because it is more rigidly balanced
		- Red-Blakc trees take smaller time to construct as they aren ot rigidly balanced
		- Height of node: length of the longest path from it to a leaf
		- leaf node is considerd to have height -1
		- Height of left tree and right tree shold not be different more than 1 or -1 --> Balanced	
		- rotation can be done in O(1)
		- Height: length of the longest path from it to a leaf
		- height = max(leftChild.height(), rightChild.height())+1

	+ sorting the sorted array
	+ it become a linked list so the O(N) for binary search tree
	+ if we convert binary search tree to balanced tree time complexity changes to O(logN) for all operations

	+ running time of BST operations depends on the height of the binary search tree.
	+ balanced tree gives best performance
	in AVL heights of the two child subtrees of any node differ by at most one
	+ another solution is red-black trees
	+ AVL trees are faster than red-black trees because they are more rigidly balanced but needs more work
	+ OS rely on these data structures


##Red black properties
	1. each node is either red or black
	2. Root node is always black
	3. all leaves NIL or NULL are black
	4. every red node must have two black child nodes and no other children it must have black parent
	5. each path from a given node to any of its descendant NIl/NULL nodes contains the same number of black nodes
	+ linux kernels relies heavily on red-black tree data strcuture
	+ Insertion is fast -> because it is not rigidly balanced and we do not bother - About making the tree as balanced as possible
	+ For insert intensive tasks use a red-black tree
	+ Exampl: java.util.TreeMap, java.util.TreeSet
	+ C++ STL: map, multipmap, multiset

	- Red-Black Tree use for insert operations --> Search is slow
	- AVL Tree good for lookup --> insert and delete operation is slow coz we need to rebalanced

##Priority Queue:
	- It is an abstract data type such as stack or queue
	- BUT each item has additional property: a priority value
	- In priority queue, item with higher priority value is processed first
	- Implemented using heaps, but it can be implemented with self balanced tree as well.
	- Very similar to queue when pop next item pop the item with higher priority
	- The concept of priority queue naturally suggest a sorting algorithms
	- Insert all the elements to be sorted into a priority queue
	- sequentially remove them: it will be the sorted order
	- Example: tree sort, heap sort

##Heap:
	- Implementation of Priority Queue
	- Binary Tree
	- minimum heap --> root node is minimum and so on
	- maximum heap --> root node in maximum and so on
	- Applications: Dijkstra's algorithm, Prims algorithm
	- Heap is different than Binary search tree in the sense that, heap does not follow the rule of smaller item on the left and larger item in the right, rather
	  it insert left first then rigth irrespective of the value.
	 - Heap Properties:
	 	- must have complete nodes
	 	- Min Heap: parent is always smaller than tha value of the child
	 	- Max Heap: parent is always greater than the value of the child
	 	- O(1) --> access
	- Maximum HEAP:
		- assign indices from left to right line by line
		- It can be implemneted as a one dimensional array
		- Access for parent i, left child is 2*i+1 and right child is 2*i+2
		- Time complexity:
			- O(N) --> for construction
			- O(logN) --> Reconstruction => O(N)
			- Delete Root Operation -> Remove item O(1), reconstruction O(logN) ==> Delete = O(logN)
			- Delete  arbitary item --> O(N)

##Heapsort:
	- Comparison based sorting
	- uses heap data structure not linear data strcutuer.
	- bit slower in practice on most machine than a well implemented quicksort
	- it has advantage of a more favorable worst case O(NlogN) runtime
	- not a stable sort
	- construction is O(N)
	- Sorting is O(NlogN)
	- Running time complexity
		- Memory Complexity = O(N)
		- Finding min/max item =O(1)
		- Insert new item = just insert O(1), conforming heap properties is O(logN) so overall time complexity is O(logN)
		- Removing Item= remvoing root node is O(1), to meet heap properties O(logN)  so overall time complexity is O(logN)

####Difference between binary search tree and heap is finding minumum and maximum is O(1) in heap but O(logN) in binary search tree as it will be a leaf node.

##Other types of heaps:
	- Binomial Heap
		- similar to binary heap but also supports quick merging of two heaps
		- It is importantant, as an implementation of the mergable heap abstract data type
		- which is priority queue + support merge operation
		- collection of tree like structure
		- inserting O(logN) time complexity of insertion in heap can be reduced to O(1) with binomial heap
	- Fibonacci Heap:
		- Faster than classic binary heap
		- Dijkstra's shortest path and Prims spanning tree algorithms work faster with Fibonacci heap compared to binary heap
		- Very hard to implement so do not worth effort
		- Unlike binary heap, it can have several children, number of children are usually kept low
		- We can achieve O(1) insert operation instead of O(logN)
		- every node has degree at most O(logN) and the size of a subtree rooted in a node of degree k is atleast F(k+2) where F(k) is the k- fibonacci.

##Time complexities:
	Find min: Binary -> O(1), Binomial -> O(1), Fibonacci --> O(1)
	Delete min: Binary -> O(logN), Binomial -> O(logN), Fibonacci --> O(logN)
	Insert -> Binary -> O(logN), Binomial -> O(1), Fibonacci --> O(1)
	Decrease Key _> Binary -> O(logN), Binomial -> O(logN), Fibonacci --> O(1)
	merge -> Binary -> N/A, Binomial -> O(logN), Fibonacci --> O(1)

##ASSOCATIVE ARRAYS:
	- Associative arrays/maps/dictionaries are abstract data types
	- composed of collection of key-value pair
	- most of the time associative array is implemented with hashtables but binary search trees can be used as well
	- aim is to reach O(1) time complexity for most of the operation
	- supported operation:
		- add key -value
		- remove
		- update
		- lookup
		- DO NOT SUPPORT SORTING so other complex implementation sare done

##HASH TABLES/DICTIONARIES:
	- uses array as underlining data strcuture
	- array index is generated using hashing of the passed key (module is simple example)
	- hash key can have collision, meaning same key is assigned to multiple values "apple", two p get same key due to hashing
	- we can resolve collison using
		- chaining --> build linked list of collision keys
		- open addressing --> generate other index for, go to another open slot
			- linear probing --> go to next
	- if hash function is nearly working, Insert, update, delete, search function in dictionary is O(1)		


##Tries:
	- When key generated Tries TST (Tenneri search tree) does not examine all the characters in the key like in hash tabl.


#Graph Algorithms:
	- G(V,E) -> are mathematical structures to model pairwise relations between given objects
	- Graph is made of vertices/nodes and edges
	- Two types:
		- directed
		- undirected
	- represented as adjacency matrix	
	- edge list reprentation
		- using vertex class with vertexName, visited, Vertex[] neighbors
	- Applications:
		- shortest path algorithm: GPS
		- graph traversing: web crawlers of google
		- Spanning trees
		- maximum flow problem: 

##Breadth First Search:
	- if we have a graph and we want to visit every node --> BFS
	- layer by layer algorithm
	- we visit each vertex exactly once neighbour by neighbour
	- running time complexity is O(V+E) and E = Edges
	- Memory complexity is not good due to lot of references
	- that is why DFS is preferred
	- It constructs a shortest path: Dijkstra algorithm does a BFS if all the edge weights are equal to 1
	- Algorithm:
		- FIFO structure
		- uses Queue abastract data type
	- Applications:
		- AI/ machine learning
		- maximum flow algorithm
		- garbage collection - Cheyen's algorithms, to maintain active references on the heap memroy
		- use BFS to detect all the references on the heap
		- Serialization/Deserialization of tree like structure

##Depth-First Search
	- widely used for graph traversal beside breadth-first search
	- it explores as far as possible alone each branch before backtracking		
	- Time complexity of traversing a graph = O(V+E)
	- Memory complexity a bit better than BFS
	- Algorithms:
		- LIFO structure
		- uses recursion or stack abstract data type
	- Applications:
		- Topoogical Ordering
		- Kosaraju algorithm of finding strongly connected components in a graph whihc can be proved to be very important in recommendation system (youtube)	
		- Detecting cycles (Checking whether a graph is a DAG or not)
		- Generating mazes or finding way out of hte maze
	- Symmetric either left or right
	
	Summary:
		BFS --> queue + layer by layer algorithm
		DFS --> stack + goeas as deep as possible in a tree	

##Memory Complexity:
	- BFS:
		- O(N)
		- used in artificial intelligence, robot movement
	- DFS
		- O(logN)
		- preferred most of the times

## SHORTEST PATH
	- Shortest path algorithm: finding a path between two vertices in a graph such that the sum of weights of its edges is minimized
		- Dijkstra algorithm
			- positive edge weights only
			- can find shortest path between A to B
			- also able to construct a shortest path tree as well
			- defines the shortest paths from a source to all the other nodes
			- asymptotically the fastest known single-source shortest-path algorithm for arbitrary directed graphs with unbounded non negative weights
			- Time complexity: O(V*logV + E)
			- It is a greedy algorithm: tries to find global optimum with the help of local minimum 
			- on every iteration we want to find the minimum distance to the next vertices possible
			- appropriate data structure: heaps, binary or Fibonacci or in general priority queue
			

		- Bellman-Ford algorithm
			- can have negative weight of edge
		- A* search
		- Floyd-Warshall algorithm
