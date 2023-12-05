from linked_list_blossom import LinkedList, Node

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList(None) for i in range(size)]
  
  def hash(self, key):
    return sum(key.encode())

  def compressor(self, hash_code):
    return hash_code % self.array_size

  # implementation of separate chaining with linked-lists  
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))

    # implementing separate chaining
    payload = Node([key, value])
    list_at_array = self.array[array_index]

    # get head node
    ll_head_node = list_at_array.get_head_node()
    # if no head_node is none insert the new node
    if ll_head_node == None:
      list_at_array.insert(payload)
    else:
      while ll_head_node:
        # pcompare keys within the hed node
        if ll_head_node.value[0] == key:
          node.value[1] = value
          return
        ll_head_node = ll_head_node.get_next_node()
      # if no key matches add new node to tail
      list_at_array.insert(payload)
    pass

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]


    ll_head_node = list_at_index.get_head_node()

    while ll_head_node:
      if ll_head_node.get_value()[0] == key:
        return ll_head_node.get_value()[1]
      ll_head_node = ll_head_node.get_next_node()
    return None


from blossom_lib import flower_definitions

# instantiating a hashmap of required size
blossom = HashMap(len(flower_definitions))
# loading data into the hashmap
for pair in flower_definitions:
  blossom.assign(pair[0],pair[1])

print("Length of the blossom HashMap: {}\n".format(len(blossom.array)))

# display resulting HashMap
i = 0
for linked_list in blossom.array:
  print("Index {0} of HashMap:\n{1}".format(i,linked_list.stringify_list()))
  i += 1

# testing retrieve function
print("Get value of rose: {0}".format(blossom.retrieve("rose")))
print("Get value of begonia: {0}".format(blossom.retrieve("begonia")))
print("Get value of loewenzahn: {0}".format(blossom.retrieve("loewenzahn")))
print(blossom.compressor(blossom.hash("loewenzahn")))
print(blossom.compressor(blossom.hash("snapdragon")))
