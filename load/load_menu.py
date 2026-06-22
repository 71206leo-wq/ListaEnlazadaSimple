from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_lista_enlazada_simple import LoadListaEnlazadaSimple


class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Menu.ui', self)
        
        self.actionLista_Enlazada.triggered.connect(self.load_lista_enlazada)
        self.actionSalir.triggered.connect(self.load_lista_enlazada)

    def load_lista_enlazada(self):
        lista_enlazada = LoadListaEnlazadaSimple()
        lista_enlazada.exec_()
        
        