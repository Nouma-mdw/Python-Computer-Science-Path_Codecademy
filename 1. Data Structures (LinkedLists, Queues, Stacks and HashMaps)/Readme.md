# 1. Blossom Project:

## Implementing HashMaps with blossom data in Python 

#### Project Description:
Given classes definitions of nodes and linked lists  (see linkedlist_blosssom.py)
the task is to implement a HashMap that takes in the data from blossom_lib.py (flowers and their meaning) 
and saves them as a map: In the map the flower is the key and the  meaning the value, meaning that every flower can have at most one meaning.
The key_value pairs get saved under an index caclulated with a hashing function ("sum(key.encode())")and a compressor adapting the index to an array length.
In case of two keys getting the same array index, a collision, the strategy to circumvent this problem and even thoug save the values in the list is a separate  chaining with linked lists.
There each time two key-value pairs have keys resulting int the same array_index, (check this for "rose" and "morning glory" in blossomproject.py), they get saved under the same array index, after each other. This is  implemented having a linked list for every index of the array.

# 2. Towers of Hanoi

## Implementing Stacks in Python to play towers of hanoi in CLI 

#### Project Description:
Using the data structure  of stacks, the towers of Hanoi game is implemented for the CLI.
Towers of Hanoi has three towers with disks that can only be moved in the according to LIFO (LAST IN FIRST OUT).
This makes stacks the structure to go  with. Additional constraints of  the game are managed with control flow.
Try playing in CLI.
