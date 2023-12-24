from collections import deque

class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes
    
  def __repr__(self):     ### version 1 ###
    return self.value
    
  # def __repr__(self):   ### version 2 ###
  #   stack = deque()
  #   stack.append([self, 0])
  #   level_str = "\n"
  #   level = 0
  #   while len(stack) > 0:
  #     node, level = stack.pop()
      
  #     if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
  #       level_str += "   "*(level-1)+ "├─"
  #     elif level > 0:
  #       level_str += "   "*(level-1)+ "└─"
  #     level_str += str(node.value)
  #     level_str += "\n"
  #     level+=1
  #     for child in node.children:
  #       stack.append([child, level])

  #   return level_str


  # def __str__(self):    #### version 3 ###
  #   stack = deque()
  #   stack.append([self, 0])
  #   level_str = "\n"
  #   while len(stack) > 0:
  #     node, level = stack.pop()
      
  #     if level > 0:
  #       level_str += "| "*(level-1)+ "|-"
  #     level_str += str(node.value)
  #     level_str += "\n"
  #     level+=1
  #     for child in reversed(node.children):
  #       stack.append([child, level])

  #   return level_str

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children
      
      
def print_tree(root):
  stack = deque()
  stack.append([root, 0])
  level_str = "\n"
  prev_level = 0
  level = 0
  while len(stack) > 0:
    prev_level = level
    node, level = stack.pop()
    
    if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
      level_str += "   "*(level-1)+ "├─"
    elif level > 0:
      level_str += "   "*(level-1)+ "└─"
    level_str += str(node.value)
    level_str += "\n"
    level+=1
    for child in node.children:
      stack.append([child, level])

  print(level_str)
      
def print_path(path):
  # If path is None, no path was found
  if path == None:
    print("No paths found!")

  # If a path was found, print path
  else:  
    print("Path found:")
    for node in path:
      print(node.value)


# Example 1
sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two] # check the inversed orer of adding children
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]   # check the inversed orer of adding children
three.children = [seven, six] # check the inversed orer of adding children


# Example 2 # comment all in
# ### TEST CODE TO PRINT TREE
# company = [
#   "Monkey Business CEO", 
#   "VP of Bananas", 
#   "VP of Lazing Around", 
#   "Associate Chimp", 
#   "Chief Bonobo", "Produce Manager", "Tire Swing R & D"]
# root = TreeNode(company.pop(0))
# for count in range(2):
#   child = TreeNode(company.pop(0))
#   root.add_child(child)

# root.children[0].add_child(TreeNode(company.pop(0)))
# root.children[0].add_child(TreeNode(company.pop(0)))
# root.children[1].add_child(TreeNode(company.pop(0)))
# root.children[1].add_child(TreeNode(company.pop(0)))
# print("MONKEY BUSINESS, LLC.")
# print("=====================")
# print_tree(root) # version 1
# # print(root) # version 2
