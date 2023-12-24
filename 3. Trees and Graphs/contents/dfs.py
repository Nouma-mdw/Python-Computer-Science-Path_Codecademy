# runtime: supposedly O(N)
# space complexity: supposedly O(N)

from collections import deque
from TreeNode import TreeNode, sample_root_node, print_path, print_tree

# print_tree(sample_root_node)

def dfs(root, target, path=()):
  path = path + (root,)       # version 1
  # path = path + (root.value,)   # version 2
  print(f"Searching node with value: {root.value}")

  if root.value == target:
    return path

  for child in root.children: # recursively calling dfs on children until all cildren are inspected 
    path_found = dfs(child, target, path)

    if path_found is not None:
      return path_found

  return None

print_tree(sample_root_node) # version 1
# print(sample_root_node) # version 2
path = dfs(sample_root_node, "F")
print("Hereafter follows the path:\n",path)
# print_path(path)

'''
LESSON RECAP
 - Using the TreeNode class to store a tree data structure.
 - Implementing a recursive method that searches for a path to a node
    with a specified value using the recursive paradigm often called 
    “divide and conquer.”
 - Default function arguments in Python.
 - Tuples, which are immutable lists, can be a convenient choice over 
   lists for recursive methods like this.
 - Python will implicitly return None from functions that
   terminate without reaching a return statement, but it can be a good
   practice to explicitly return None when other components expect None to be returned sometimes.
'''

