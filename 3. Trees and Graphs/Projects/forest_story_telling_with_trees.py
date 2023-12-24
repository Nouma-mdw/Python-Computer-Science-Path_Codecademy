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