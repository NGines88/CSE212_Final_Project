# import deque 
from collections import deque

# create a list
my_list = deque(['A', 'B', 'C', 'D', 'E'])

# insert an item (value) into the list
def remove_from_list(priority):
    # if the priority is 100, insert at the beginning
    if priority == 100:
        my_list.popleft()
    # insert into the middle
    elif priority == 50:
        middle = len(my_list) / 2
        del my_list[int(middle)]
    # insert at the end
    elif priority == 10:
        my_list.pop()
    
    return my_list
        
print(remove_from_list(50))
print(remove_from_list(100))
print(remove_from_list(10))
print(remove_from_list(50))        
print(remove_from_list(100))