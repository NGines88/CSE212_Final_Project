
my_stack = []

my_string = "Star Wars"

def add_to_stack():
    for i in range(len(my_string)):
        my_stack.append(my_string[i])

def get_latest():
    for i in range(0, 4):
        print(my_stack.pop())
        
add_to_stack()
get_latest()