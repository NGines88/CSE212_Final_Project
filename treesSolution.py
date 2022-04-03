# import bintrees
from bintrees import AVLTree

# Create an unordered object with key/value pairs
my_object = {'E':5, 'F':6, 'B':2, 'D':4, 'A':1, 'C':3}

# Create the tree using the object
my_tree = AVLTree(my_object)

# Prints each highest item until no higher item than the lowest exists
def print_tree(k, v):
    print(my_tree.pop_max())
my_tree.foreach(print_tree)

