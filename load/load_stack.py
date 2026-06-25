from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.stack import Stack

class LoadStack(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Stack.ui', self)
        self.stack = Stack()
        
        self.btn_push.clicked.connect(self.push)
        self.btn_pop.clicked.connect(self.pop)
        self.btn_top.clicked.connect(self.top)
        self.btn_print.clicked.connect(self.print_stack)
        self.btn_salir.clicked.connect(self.salir)
        
    def push(self):
        elemento = self.txt_dato.text()
        self.stack.push(elemento)
        self.txt_resultado.setText(f"Elemento {elemento} agregado al principio de la pila")
        
    def pop(self):
        elemento = self.stack.pop()
        if elemento is None:
            self.txt_resultado.setText(f"La pila esta vacia")
        else:
            self.txt_resultado.setText(f"Elemento {elemento} eliminado")
            
    def top(self):
        elemento = self.stack.top_of_stack()
        if elemento is None:
            self.txt_resultado.setText(f"La pila esta vacia")
        else:
            self.txt_resultado.setText(f"Elemento {elemento} en la pila")
            
    def print_stack(self):
        texto_lista = self.stack.print_of_stack()
        self.txt_resultado.setText(f"Contenido de la Pila:\n{texto_lista}")
        return texto_lista
        
    def salir(self):
        self.close()
        