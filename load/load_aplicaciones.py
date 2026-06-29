from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.aplicaciones import Aplicaciones

class LoadAplicaciones(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Aplicaciones.ui', self)
        self.btn_convertir.clicked.connect(self.convert_infix_to_postfix)
        
    def convert_infix_to_postfix(self):
        # Instanciamos tu nueva clase Aplicaciones
        procesador = Aplicaciones()
        
        # Ejecutamos el método de conversión
        texto_posfijo = procesador.convert_infix_to_postfix(self.txt_infijo.text())
        
        # Mostramos el resultado en la interfaz gráfica
        self.lbl_resultado.setText(texto_posfijo)
        
        
        
    
    