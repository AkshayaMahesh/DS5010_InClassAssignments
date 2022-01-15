class Stack:
    # Initialize method of objects
    def __init__(self, capacity):
        self.container = []
        self.capacity = capacity
# Method to return the elements present in the stack
    def __len__(self):
        return len(self.container)
# Method to return if the stack is at full capacity
    def is_full(self):
        if len(self.container) == self.capacity:
            return True
        else:
            return False
# Method to push items to stack
    def push(self, item):
        if len(self.container) < self.capacity:
            self.container.append(item)
        else:
            print("Stop! I am at the capacity")
# Method to return the items in a stack
    def __str__(self):
        stack_output = ''
        for i in self.container:
            stack_output = stack_output + i + ' '

        return stack_output
#driver code
a_stack=Stack(3)
a_stack.push('a')
a_stack.push('b')
a_stack.push('c')
a_stack.push('d')
a_stack.push('e')
print("The items in the Stack are: ",a_stack)

