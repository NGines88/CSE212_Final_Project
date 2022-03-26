# Linked-Lists

In order to better understand what a linked list is, let's take a quick look at an array. There are two different kinds of arrays: Fixed length, and dynamic. Dynamic arrays allow us to add as many items as we want (to a certain point) without needing to know exactly how big our array will be (in other words, it is not fixed to a length of `n` elements). Linked lists are similar to dynamic arrays in the sense that they are not fixed in size, and we can easily add and remove items from them. 

The biggest difference between a dynamic array and a linked list is how the data is stored. Dynamic arrays store information directly next to each other in memory. This allows for quick access, but can be limited by how much memory they are allowed to use before overflowing into addressed that are already allocated to something else. A linked list will store an item anywhere there is free space in memory, essentially allowing us to insert as many items in a list as our operating system and hardware will allow. 

This flexibility and convenience does come with a few extra bits of information that need to be kept track of. Each item in the list has two pointers that point to the location in memory of the items in front/behind it in the list. These are called the 'next' and 'previous' pointers. The first item in a linked list is called the `head,` and the last item is called the `tail`. 

## Speed Comparison

Operation | Dynamic Array | Linked List
-- | -- | --
Insert at Front | O(n) | O(1)
Remove at Front | O(n) | O(1)

When dealing with the beginning of a list, the list can instantly access the element without having to iterate through like the dynamic array. This is beneficiary when speed is criticial (such as a priority queue for incoming network operations on a server).

## How a Linked List Works

We can easily traverse a list by using a nodes (or items) `.next` pointer. This will point to the node directly after the `current` node. Here is an example: 
`next_item = current.next`
Similarly, we can go backwards through a list by using: `prev_item = current.prev`. Traversing forwards through an entire list can be done by starting at the head, and pointing to the next node until no next pointer exists. We can traverse backwards in a similar manner by starting at the tail and using the previous pointer. 

Inserting and deleting nodes from a list requires a few more steps than just a simple append or delete function call, as we have to make sure our pointers are properly set for the surrounding nodes. 

Here is how we would insert an item into the middle of the list, directly after the node `current_node`: 

1. Using `new_node` and `current_node`, set `new_node.prev` to `current_node`.
2. Set `new-node.next` to `current.next`.
3. Set `current.next.prev` to `new_node`. 
4. Set `current.next` to `new_node`.

Removing an item from a list is similar to adding one, in the sense that we need to make sure we properly set the pointers of the other nodes. To remove an item from the middle of the list, we would:

1. Set `current.next.prev = current.prev`.
2. Set `current.prev.next = current.next`. 

## Example of Using a Linked List in Python

Now that we know the fundamentals, let's put our knowledge into practice. We will be using Python's built in Linked list called `deque()`. 

The library uses the following syntax for inserting/removing the head of a list:

Insert Head: `.appendleft()`

Remove Head: `.popleft()`

The following code takes in a given value and a priority of 100, 50, or 10 (with 100 being the highest priority) and places it into a location in the list based on its priority.  

```python
# import deque 
from collections import deque

# create a list
my_list = deque()

# insert an item (value) into the list
def prioritize(value, priority):
    # if the priority is 100, insert at the beginning
    if priority == 100:
        my_list.appendleft(value)
    # insert into the middle
    elif priority == 50:
        middle = len(my_list) / 2
        my_list.insert(int(middle), value)
    # insert at the end
    elif priority == 10:
        my_list.append(value)
    
    return my_list
        
print(prioritize("D", 10))
print(prioritize("B", 100))
print(prioritize("A", 100))
print(prioritize("E", 10))        
print(prioritize("C", 50))


```

## Coding Challenge

Write a function that deletes an item from a list based on the priorities given in the example above. You will use the following as your list: `my_list = deque(['A', 'B', 'C', 'D', 'E'])`. Run your function with priorities that will yield the following output:

deque(['A', 'B', 'D', 'E'])

deque(['B', 'D', 'E'])

deque(['B', 'D'])

deque(['B'])

deque([])

[Solution](remove_from_list.py)