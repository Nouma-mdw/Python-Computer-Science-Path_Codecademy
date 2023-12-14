class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node

  # INSERT method used in stringify_list
  def get_head_node(self):
    return self.head_node
  # End of INSERTION
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node): # maybe too many iterations
      # Would't 'while current_node.get_next_node()' do the job?
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  # INSERT stringify for visualization
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    if current_node is None:
      return None
    i = 0
    while current_node:
      if current_node.get_value() != None:
        string_list += str("\tnode_{0}: {1}\n".format(i,current_node.get_value()))
      current_node = current_node.get_next_node()
      i += 1
    return string_list[:-1]
  # END of INSERTION

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()

