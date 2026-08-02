from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QGraphicsScene, QWidget
from PyQt5 import uic
from load.load_lista_enlazada_simple import LoadListaEnlazadaSimple
from load.load_stack import LoadStack
from load.load_aplicaciones import LoadAplicaciones
from load.load_queue import LoadQueue
from load.load_banco import LoadBanco
from load.load_gestion_impresion import LoadGestionImpresion
from load.load_arbol import ExpressionTreeWindow
from load.load_graph import LoadGraph


class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Menu.ui', self)
        
        self.actionLista_Enlazada.triggered.connect(self.load_lista_enlazada)
        self.actionSalir.triggered.connect(self.load_lista_enlazada)
        self.actionStack.triggered.connect(self.load_stack)
        self.actionAplicaciones.triggered.connect(self.load_aplicaciones)
        self.actionQueue.triggered.connect(self.load_queue)
        self.actionBanco.triggered.connect(self.load_banco)
        self.actionGestion_Impresion.triggered.connect(self.load_gestion_impresion)
        self.actionArbol_expresiones.triggered.connect(self.load_arbol)
        self.actionGrafo.triggered.connect(self.load_graph)

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
    
    def load_banco(self):
        banco = LoadBanco()
        banco.exec_()
        
    def load_gestion_impresion(self):
        gestion_impresion = LoadGestionImpresion()
        gestion_impresion.exec_()
        
    def load_arbol(self):
        self.arbol = ExpressionTreeWindow()
        self.arbol.show()
        
    def load_graph(self):
        self.graph = LoadGraph()
        self.graph.show()   