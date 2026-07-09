from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.queue import Queue

class LoadQueue(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Queue.ui', self)
        self.queue = Queue()
        
        self.btn_enqueue.clicked.connect(self.enqueue)
        self.btn_dequeue.clicked.connect(self.dequeue)
        self.btn_first.clicked.connect(self.firstQueue)
        self.btn_last.clicked.connect(self.lastQueue)
        self.btn_print.clicked.connect(self.print_queue)
        self.btn_salir.clicked.connect(self.salir)
        
    def enqueue(self):
        elemento = self.txt_dato.text()
        self.queue.enqueue(elemento)
        self.txt_resultado.setText(f"Elemento {elemento} agregado al principio de la cola")

    def dequeue(self):
        elemento = self.queue.dequeue()
        if elemento is None:
            self.txt_resultado.setText(f"La cola esta vacia")
        else:
            self.txt_resultado.setText(f"Elemento {elemento} eliminado")
            
    def firstQueue(self):
        elemento = self.queue.firstQueue()
        if elemento is None:
            self.txt_resultado.setText(f"La cola esta vacia")
        else:
            self.txt_resultado.setText(f"Elemento {elemento} en la cola")
            
    def lastQueue(self):
        elemento = self.queue.lastQueue()
        if elemento is None:
            self.txt_resultado.setText(f"La cola esta vacia")
        else:
            self.txt_resultado.setText(f"Elemento {elemento} en la cola")

    def print_queue(self):
        texto_lista = self.queue.printQueue()
        self.txt_resultado.setText(f"Contenido de la cola:\n{texto_lista}")
        return texto_lista
        
    def salir(self):
        self.close()