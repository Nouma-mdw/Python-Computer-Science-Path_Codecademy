from linkedlist_blossom import LinkedList, Node

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
def execute():

  print("Hi there,\nthis little programm is for you to see the data structure of a hashmap\nand check how the separate chaining strategy works")
  print('''If you want to quit this program, just input anything thing other than 'y'.
        ''')

  start = input("Do you want to take a glance? (y = yes) ")


  if start != "y":
    print("Well then have a nice time")
    return
  
  

  print("\nFirst let's take a look at the data we want to save in the hashmap.\n\n")
  for item in flower_definitions:
    print(item)
  
    # instantiating a hashmap of required size
  blossom = HashMap(len(flower_definitions))
  # loading data into the hashmap

  if input("\n\nIn the backend the hashmap has been created. Want to take a look? (y = yes) ") != "y":
    print("By, bye")
    return

  print("This is the empty hashmap based on an array:\n\n")
  i = 0
  for linked_list in blossom.array:
    print("Index {0} of HashMap:\n{1}".format(i,linked_list.stringify_list()))
    i += 1
  
  if input("Above you see the empty hashmap as big as the data to fill it with. To better appreciate the structure two more versions of the hashmap will be displayed for you to compare.\
        \n2. The hashmap filled was filled partially in the backend.\
        \n3. hashmap filled partially\
           \n want to check now? (y = yes) ") != 'y':
    print("By, bye")
    return
  for i in range(0,4):
    pair = flower_definitions[i]
    blossom.assign(pair[0],pair[1])
  
  i = 0
  for linked_list in blossom.array:
    print("Index {0} of HashMap:\n{1}".format(i,linked_list.stringify_list()))
    i += 1

  if input("\n\nThis is the 2. version of the  hashmap.Note that different 'fields' of the array are only filled with one node (node_0) and no more. Ready to continue? (y = yes) ") != "y":
    print("By, bye")
    return

  for i in range(4,len(flower_definitions)):
    pair = flower_definitions[i]
    blossom.assign(pair[0],pair[1])
  print("Length of the blossom HashMap: {}\n".format(len(blossom.array)))

  # display resulting HashMap
  i = 0
  for linked_list in blossom.array:
    print("Index {0} of HashMap:\n{1}".format(i,linked_list.stringify_list()))
    i += 1
  
  if input("\n\nNow the hashmap is full. Compare it to the original data of to asnwer the following questions:\
           \n1. How many datafields are in under one index?\
           \n2. How many fields are empty. If we were to sort every value into one field. Would they be full?\
           \nAnsered the questions and want to continue? ") != "y":
    print("By, bye")
    return
  print("\nWell, the different flowers and their meanings are stored acording to a hashfunction. \
        \nTo flowers that have the same hash, share the same index. So data got sorting according to the hash of the keys (flowers names).\
        \nFor the empty indexes, there were no keys (flowernames) that the hash function mapped to. This is the separate chaining strategy.\
        \nIt helps to deal with multiple keys having the same hash.")
  

  # testing retrieve function
  if input("Check this out?") != 'y':
    return print("Bye bye")
  print("\n\nHere you see the hash for morning glory {} and for rose {}".format(blossom.compressor(blossom.hash("morning glory")),blossom.compressor(blossom.hash("rose"))))
  print("Compare with their index and position in the third hashmap in the above table.")

  # testing retrievel function
    # print("Get value of rose: {0}".format(blossom.retrieve("rose")))
    # print("Get value of begonia: {0}".format(blossom.retrieve("begonia")))
    # print("Get value of loewenzahn: {0}".format(blossom.retrieve("loewenzahn")))

execute()