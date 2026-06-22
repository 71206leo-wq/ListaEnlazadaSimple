from estructuras.lineales.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        #Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            #Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            #Si la lista no está vacía, el nuevo nodo apunta a la cabeza actual
            new_node.next = self.head
            #Luego, la cabeza se actualiza para ser el nuevo nodo
            self.head = new_node
    
    def print_linked_list(self):
        temp = self.head
        resultado = "Head ->"
        while temp is not None:
            resultado = resultado + " " + str(temp.data) + "->"
            temp = temp.next
        resultado = resultado + "<- Tail"
        return resultado
        
    
    def insert_at_end(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        #Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            #Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            #Si la lista no está vacía, el nuevo nodo apunta a la cola actual
            self.tail.next = new_node
            #Luego, la cola se actualiza para ser el nuevo nodo
            self.tail = new_node
    
    def search(self, data): 
        #Paso 1: Iniciar un nodo temporal en la cabeza de la lista
        temp = self.head
        #Paso 2: Recorrer la lista mientras el nodo temporal no sea nulo
        while temp is not None:
            #Si el dato del nodo es igual al buscado, se devuelve True
            if temp.data == data:
                return True
            #Si no, se pasa al siguiente nodo
            temp = temp.next
        #Si no se devuelve False
        return False
    
    def delete_at_beginning(self):
        #Paso 1: Verificar si la lista no está vacía
        if self.head is None:
            print("La lista está vacía")
            
        elif self.head == self.tail:
            #Si la lista solo tiene un nodo, se actualiza la cabeza y la cola
            self.head = None
            self.tail = None
            
        else:
            #Si la lista tiene más de un nodo, se elimina el nodo inicial y se actualiza la cabeza
            temp = self.head
            
            while temp.next != self.tail:
                temp = temp.next
                
            self.tail = temp
            self.tail.next = None
            
    def delete_at_end(self):
        #Paso 1: Verificar si la lista no está vacía
        if self.head is None:
            print("La lista está vacía")
            
        elif self.head == self.tail:
            #Si la lista solo tiene un nodo, se actualiza la cola y la cabeza
            self.head = None
            self.tail = None
            
        else:
            #Si la lista tiene más de un nodo, se elimina el nodo final y se actualiza la cola
            temp = self.head
            
            while temp.next != self.tail:
                temp = temp.next
                
            self.tail = temp
            self.tail.next = None