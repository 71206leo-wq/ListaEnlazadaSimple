from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5 import uic
from estructuras.lineales.lista_enlazada_simple import LinkedList

class LoadListaEnlazadaSimple(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Listas_Enlazadas.ui', self)
        self.lista_enlazada = LinkedList()
        
        self.btn_agregar_inicio.clicked.connect(self.agregar_inicio)
        self.btn_agregar_final.clicked.connect(self.agregar_final)
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_imprimir.clicked.connect(self.imprimir)
        self.btn_eliminar_inicio.clicked.connect(self.eliminar_inicio)
        self.btn_eliminar_final.clicked.connect(self.eliminar_final)
        self.btn_salir.clicked.connect(self.salir)
        
    def agregar_inicio(self):
        elemento = self.txt_dato.text()
        self.lista_enlazada.insert_at_beginning(elemento)
        self.txt_resultado.setText(f"Elemento {elemento} agregado al principio de la lista")
        
    def agregar_final(self):
        elemento = self.txt_dato.text()
        self.lista_enlazada.insert_at_end(elemento)
        self.txt_resultado.setText(f"Elemento {elemento} agregado al final de la lista")
        
    def buscar(self):
        elemento = self.txt_dato.text()
        encontrado = self.lista_enlazada.search(elemento)
        if encontrado:
            self.txt_resultado.setText(f"Elemento {elemento} encontrado")
        else:
            self.txt_resultado.setText(f"Elemento {elemento} no encontrado")
            
    def imprimir(self):
        texto_lista = self.lista_enlazada.print_linked_list()
        self.txt_resultado.setText(f"Contenido de la Lista enlazada:\n{texto_lista}")
    
        
    def eliminar_inicio(self):
        elemento = self.txt_dato.text()
        encontrado = self.lista_enlazada.search(elemento)
        if encontrado:
            self.lista_enlazada.delete_at_beginning()
            self.txt_resultado.setText(f"Elemento {elemento} eliminado")
            
    def eliminar_final(self):
        elemento = self.txt_dato.text()
        encontrado = self.lista_enlazada.search(elemento)
        if encontrado:
            self.lista_enlazada.delete_at_end()
            self.txt_resultado.setText(f"Elemento {elemento} eliminado")
            
    def salir(self):
        self.close()
        