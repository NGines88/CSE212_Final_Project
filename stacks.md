# Stacks

A stack is a data structure that can be summarized as, "First In, Last Out." When multiple items are added to a stack, the last item added will also be the first item removed. Let's say we have a stack with 10 items. When item 11 is appened, it will be the first item that gets removed from the stack. Item number 1 will be the last item to be removed. This is in stark contrast to the Queue data structure that has a "First In, First Out" method of operation. 

Because of their simplicity, searching for a value in a stack is done in O(n) time. This means that the computer will need to start at the beginning of the stack, and loop through each item individually until it finds the value it is searching for. 

## Examples of Stacks
Stacks are used when we want to maintain a history of or a collection of items, but want easy and quick access to the latest item first. We can visualize a Stack by comparing it to this real world example: An actual 'stack' of bricks. If we stack one brick on top of another, the only way we can remove a brick without our stack collapsing is to start from the top and work our way down. 

Here's an example of a stack in action: Say we are developing a video game that allows us to build a Roller Coaster piece by piece. We start with the first track piece, and keep adding pieces as we desire. After building a few more track pieces, we realize our roller coaster pieces went too high and our coaster car does not have enough speed to make it over them. With a stack, we can simply remove the last piece we added, and continue removing the latest pieces we added until we reach a point where our coaster is low enough for our coaster car. 

## How to Use a Stack
Here's an example of adding an item to a stack in code: 
```python
my_stack = []

my_string = "Star Wars"

def add_to_stack():
    for i in range(len(my_string)):
        my_stack.append(my_string[i])

        
add_to_stack()
```
In this example, every letter in the string "Star Wars" was added to 'my_stack'.

We use `.append()`  to add an item to the stack, and `.pop()` to remove the item from the top of the stack. 

We can also use `len(stack)` to return the number of elements in our stack in O(1) time (the stack only needs to be iterated through a single time). 

## Coding Challenge
Write a program that takes the stack given above, and prints out the last 4 letters. The output should be as follows.

s

r

a

w

Only view the provided the solution after you have made an attempt to solve: [Solution](stack_solution.py)

