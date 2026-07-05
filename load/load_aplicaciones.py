from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.aplicaciones import Aplicaciones, EvaluadorPosfija

class LoadAplicaciones(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Aplicaciones.ui', self)
        self.btn_convertir.clicked.connect(self.convert_infix_to_postfix)
        self.btn_evaluar.clicked.connect(self.procesar_evaluacion)
        
    def convert_infix_to_postfix(self):
        # Instanciamos tu nueva clase Aplicaciones
        procesador = Aplicaciones()
        
        # Ejecutamos el método de conversión
        texto_posfijo = procesador.convert_infix_to_postfix(self.txt_infijo.text())
        
        # Mostramos el resultado en la interfaz gráfica
        self.lbl_resultado.setText(texto_posfijo)
        


    def procesar_evaluacion(self):
        # Instanciamos tu clase EvaluadorPosfija
        self.evaluador = EvaluadorPosfija()
        
        #Leer la etiqueta de la expresión posfija convertida
        texto_convertido = self.lbl_resultado.text()
        
        # Ejecutamos el método de evaluación
        resultado = self.evaluador.evaluar(texto_convertido)
        
        # Mostramos el resultado en la interfaz gráfica
        self.lbl_resultado2.setText(str(resultado))
        
        
    
    