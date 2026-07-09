from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5 import uic
from load.load_lista_enlazada_simple import LoadListaEnlazadaSimple
from load.load_stack import LoadStack
from load.load_aplicaciones import LoadAplicaciones
from load.load_queue import LoadQueue


class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Menu.ui', self)
        
        self.actionLista_Enlazada.triggered.connect(self.load_lista_enlazada)
        self.actionSalir.triggered.connect(self.load_lista_enlazada)
        self.actionStack.triggered.connect(self.load_stack)
        self.actionAplicaciones.triggered.connect(self.load_aplicaciones)
        self.actionQueue.triggered.connect(self.load_queue)
        
        
        

    def load_lista_enlazada(self):
        lista_enlazada = LoadListaEnlazadaSimple()
        lista_enlazada.exec_()
        
    def load_stack(self):
        stack = LoadStack()
        stack.exec_()
        
    def load_aplicaciones(self):
        aplicaciones = LoadAplicaciones()
        aplicaciones.exec_()
        
    def load_queue(self):
        queue = LoadQueue()
        queue.exec_()
    