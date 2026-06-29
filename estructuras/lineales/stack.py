from estructuras.lineales.nodo import Node

class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.top is None:
            return None
        else:
            eliminated_value = self.top.data
            self.top = self.top.next
            return eliminated_value
        
    def top_of_stack(self):
        if self.top is None:
            return None
        else:
            return self.top.data
        
    def print_of_stack(self):
        temp = self.top
        mensaje=""
        if temp is None:
            print("The stack is empty")
            return
        else:
            print("The stack is not empty")
            while temp is not None:
                mensaje += temp.data + "->"
                temp = temp.next
        return mensaje
    
                