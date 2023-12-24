The next two algorithms traverse a tree in search for a value.
Their implementations reuire the concept pf a frotnier.
Each time a value is analzed, it's children get added to the  nodes that are next to be considered.
These nodese build the frontier.
Depending on the underlying datastructure of this frontier (queue or stack)
we end up with breadth-first-search or depth-first-search.
For both it is true, that after each node got inspected, it get's kicked out of the frontier
and it's children get added.


BFS (breadth-first-search)

- based un queue structure FIFO (first in first out)
  after every node, it's children
- iterative implementation using a queue:
	1. starts a root node and initiates a frontiert of paths consisting of root node
	2. loops while frontier ins't empty, poping frontiers last path and inspecting it's last node
	3. if matching goal_value, path is returned, otherwise children of last node 
		are individually added to path copies creating and left appended to the frontier (queue with FIFO)
- time complexity:
	O(N) with N number of nodes in tree (worst case - inspect every node)
- space complexity: (according to lesson, i doubt it)
	O(N) with N number of nodes in tree (worst case - save every node)




DFS (deep-first_search)
- based on stack structure LIFO (last in first out)
- recursive implementation:
	1. starts at root node and gets called recursively on all root's  children
	2. it splits the tree up into subtrees roots children as subtree roots
	3. func input is a root node and a goal_value to be found

- iterative implementation uses stack of references for unexplored nodes
	1. maintains stack of accessed nodes for unexplored siblings
	2. path: whereas the recursive version saves the path in the call stack
		the iterative version requires a stack implementation

|--> both implementations (recursive and iterative) have the same time and space  complexity
- time complexity: 
	O(N) with N - number of nodes in tree (worst case - inspect every node)

- space complexity:
	O(N) with N - number of nodes in tree (worst case . save a reference to every node in stack)

- practical considerations:
Codecademy: "DFS can be used for searching for objects in a data structure like files in a file system. More abstract applications can be found in domains like artificial intelligence, for example, searching through possible moves in a game like chess, or searching for a path through a maze."

decision simulation:
"Depth-First Search is an exhaustive method, so consider that some trees may be infinitely large or just large enough that they are practically impossible to completely traverse. In practice, we can limit the depth allowed to search by the algorithm. Consider something like an algorithm for playing chess. We can simulate a series of moves and responses, but the search space may be so large that no modern computer could reasonably explore all possible paths."


# Algorithmic Approach 1
Divide and Conquer:

- three steps: 
	1) divide into subproblems, 
	2) conquer subproblems, 
	3) combine solution to subproblems
- merge_sort and quicksort are examples for divide and conquer


time and space complexity
- from Codecademy """
There is no single time or space complexity that can describe all divide-and-conquer algorithms. However, we can follow these general rules to determine the big-O runtime of a specific algorithm:

Because the problem is divided into at least 2 subproblems at each step, the number of steps needed to divide the problem is log(n).
The cost of solving and merging the subproblems is a factor as well. This is often multiplied by the cost of division to get the overall runtime.
For merge sort, division takes O(log(n)) time, and combining the sorted sublists takes O(n) time. Therefore, merge sort has a big-O runtime of O(nlog(n)).

The space complexity also varies from algorithm to algorithm. Divide-and-conquer usually requires more space than other paradigms due to the overhead of the recursion stack."""

binary search on sorted arrays



Transferring tree and graph structures into linear lists:
The main tak away here is that it is possible to translate
tree and graph structures into arrays or lists by...
1) enumerating nodes according to their relationships parent-child (for trees) and paths of vertices (for graphs)
2) these enumerations are then used, to relate each node/vertex to an index of the list.
3) besides saving the node/vertex to the list, it is important to save the relations of vertex, offen saved as numerical relations
(e.g. MaxHeaps are trees with 2 nodes per parent, in which for every node with index i, it's children (max 2) have indices "2*i" and "2*i+1")


# ALgorithmic Approach 2
Greedy Algorithms

When to use greedy algorithms
We must be careful when using greedy algorithms because they are not guaranteed to be correct. A problem that can be correctly solved by a greedy algorithm must satisfy these two properties:

	1) Optimal substructure property - the optimal solution for the problem contains optimal solutions to the sub-problems.
	2) Greedy property - the global optimal solution can be reached by making locally optimal choices.
Pros and Cons
Greedy algorithms have the following advantages:

	+ Easy to understand and implement.
	+ Time and space complexities are easy to analyze.
	+ Perform better than other paradigms like divide-and-conquer.

However, there are some crucial disadvantages:

	- Most greedy algorithms fail to find the global optimal solution.
	- Hard to prove the correctness of a greedy algorithm.
	- If a greedy algorithm is proven to be correct, it generally becomes the best method for solving optimization problems because it is faster than other techniques. Some of the common applications for greedy algorithms include pathfinding, graph 		search, and data compression.


Greedy example_ Dijkstras Algorithm

Congratulations on grasping a conceptual understanding of Dijkstra’s Algorithm!

Here’s a quick recap of what you’ve learned:

Dijkstra’s algorithm is an algorithm to find all of the shortest distances between a start vertex and the rest of the vertices in a graph.
The algorithm works by keeping track of all the distances and updating the distances as it conducts a breadth-first search.
Dijkstra’s algorithm runs in O((E+V)log V).