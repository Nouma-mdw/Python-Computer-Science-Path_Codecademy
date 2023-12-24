'''
THE PROBLEM:
Version 1: combining dance figures
to express yourself you want to combine figures and steps in your own creative way.
Now steps aren't sorte in a tree structure. They a steps, like a list of steps.
So how can you  ombine them?
Modelling:
Given each step has different characteristics (position, balance_leg, momentum_direction),
to combine two steps, the end of one has  to match the characteristics of the other.
So we can desribe each step as single node having not one value, but a start_value and end_value
both describing respectively the characteristics of the step when it starts and when it ends.
O top each node has two references: the prior_list referencing to all steps which can set up this one
and the after_list referencing all steps to combine after performing this step.

Algorithm expectation:
Input shall be an iterable with a list of nodes and a limit.
The output shall be combinations of steps from the list, up to the limit.
--> maybe the start list isn't necessary?
For dancers looking out for new combinations it would be useful.

Architectural requirements:
given the inputs of a list of nodes and  a limit for combination length, and
the expectation of combining nodes based on start and end characteristics.
we might:
  - make nested for loops that test combinations for every node in the list:
    - option 1: the inner loops searches for the second step to combine with the outer loops variable
      allowing a maximum length of two and saving combinations of length two in an array
    - option 2: the inner loop searches for the following step based on the last step of the combination
  
'''

######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self


    # # while loop according to instructions
    # while story_node.choices:
    #   # print(story_node.story_piece)
    #   choice = input("Enter 1 or 2 to continue the story: ")
    #   if choice not in ["1","2"]:
    #     print("Invalid input. Try again after the part repetition: ")
    #   else:
    #     chosen_index = int(choice)
    #     chosen_index -= 1
    #     chosen_child = story_node.choices[chosen_index]
    #     print(chosen_child.story_piece)
    #     story_node = chosen_child
    # print(story_node.story_piece)

    # I'm deviating from instruction 22 for better functionality and legibility
    
    while story_node.choices:
      choice = input(story_node.story_piece) # print and get input in one line
      if choice.isdigit and int(choice) in range(1, len(self.choices) + 1):
        # allows for different number of options
        story_node = story_node.choices[int(choice) - 1]
        # .traverse() called from root requires to call .choices[...] on story_node to advance story, called on self.choices[...] we get stuck
      else:
        choice = input("Invalid input, please enter 1 or 2. ")
    print(story_node.story_piece)

######
# VARIABLES FOR TREE
######
# root TreeNode
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1) Roar back!
2) Run to the left...
""")

# # testing input with user name
# user_choice = input("What is your name? ")
# print(user_choice)

# choices from the root TreeNode
choice_a = TreeNode('''
The bear is startled and runs away.
Do you:
1) Shout 'Sorry bear!'
2) Yell 'Hooray!'
''')
choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

# adding choices to root
story_root.add_child(choice_a)
story_root.add_child(choice_b)

# second level childs for child_a
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

# second level childs for child_a
choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")

choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

# adding 2nd level choices
  ## for choice_a
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

  ## for choice_b
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)


######
# TESTING AREA
######
print("Once upon a time...")
# print(story_root.story_piece)
story_root.traverse()