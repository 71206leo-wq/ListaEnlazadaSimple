from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.gestion_impresion import GestorImpresion
from estructuras.lineales.queue import Queue

class LoadGestionImpresion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/GestionImpresion.ui', self)
        self.gestor = GestorImpresion(Queue())  # Instancia limpia conectada a tu cola
        self.btnAgregar.clicked.connect(self.agregar_trabajo)
        self.btnImprimir.clicked.connect(self.procesar_siguiente)
        self.btnConsultarFrente.clicked.connect(self.consultar_frente)
        self.actualizar_pantalla()
        
    def agregar_trabajo(self):
                        usuario = self.txtUsuario.text()
                        documento = self.txtDocumento.text()
                        paginas = self.spinPaginas.value()
        
                        exito, mensaje = self.gestor.agregar_trabajo(usuario, documento, paginas)
                        self.lblMensajes.setText(mensaje)
        
                        if exito:
                            self.txtUsuario.clear()
                            self.txtDocumento.clear()
                            self.spinPaginas.setValue(1)
                            self.actualizar_pantalla()

    def procesar_siguiente(self):
                            exito, mensaje = self.gestor.procesar_siguiente()
                            self.lblMensajes.setText(mensaje)
                            self.actualizar_pantalla()

    def consultar_frente(self):
                            frente = self.gestor.obtener_frente()
                            self.lblFrente.setText(f"Frente actual: {frente}")

    def actualizar_pantalla(self):
                            # Actualizar la etiqueta del total de pendientes
                            self.lblTotalPendientes.setText(f"Trabajos en cola: {self.gestor.obtener_total()}")
                            
                            # Renderizar los elementos vigentes de la estructura enlazada en el QListWidget (Orden FIFO)
                            self.listTrabajos.clear()
                            for trabajo_str in self.gestor.listar_trabajos():
                                self.listTrabajos.addItem(trabajo_str)
                                
                            # Actualiza el indicador visual del frente de forma automática
                            self.consultar_frente()
                            
    # === AGREGAR AL FINAL DE TU CLASE DE INTERFAZ VIGENTE ===

    def evento_boton_agregar(self):
        """Nueva función conectada al botón Agregar de la interfaz."""
        usuario = self.txtUsuario.text()
        documento = self.txtDocumento.text()
        paginas = self.spinPaginas.value()
        
        # Llama a la nueva función de validación
        exito, mensaje = self.gestor.validar_y_encolar(usuario, documento, paginas)
        self.lblMensajes.setText(mensaje) # Muestra el resultado en pantalla
        
        if exito:
            # Solo limpia los campos si los datos fueron correctos y aceptados
            self.ui.txtUsuario.clear()
            self.ui.txtDocumento.clear()
            self.ui.spinPaginas.setValue(1)
            self.actualizar_pantalla()

    def evento_boton_imprimir(self):
        """Nueva función conectada al botón Imprimir Siguiente de la interfaz."""
        # Llama a la nueva función de validación de cola vacía
        exito, mensaje = self.gestor.validar_e_imprimir()
        self.lblMensajes.setText(mensaje) 
        
        self.actualizar_pantalla()