from estructuras.lineales.nodo import Node
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        
    def is_empty(self):
        return self.first is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
            return
        else:
            self.last.next = new_node
            self.last = new_node
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            eliminated_value = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return eliminated_value
        
    def firstQueue(self): 
    # Consulta el primer elemento sin eliminarlo 
        if self.is_empty():
            return None 
        else: 
            return self.first.data
        
    def lastQueue(self):
        # Consulta el último elemento sin eliminarlo
        if self.is_empty():
            return None
        else:
            return self.last.data
        
    def printQueue(self):
            temp = self.first
            mensaje = ""
            if temp is None:
                print("La cola está vacía.")
                return mensaje
            else:
                while temp is not None:
                    # Formateamos el cliente para mostrarlo visualmente en la cola
                    mensaje += f"[Turno {temp.data['turno']}]"
                    if temp.next is not None:
                        mensaje += " -> "
                    temp = temp.next
                print(mensaje)
                return mensaje
            
    
    
    
    
    
