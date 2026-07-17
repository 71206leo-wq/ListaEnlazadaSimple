from datetime import datetime
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.banco import Banco
        
class LoadBanco(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Banco.ui', self)
        self.sistema_banco = Banco()
        self.btn_agregar.clicked.connect(self.agregar_cliente)
        self.btn_atender.clicked.connect(self.atender_cliente)
        self.btn_cerrar.clicked.connect(self.cerrar_banco)
        

            
    def agregar_cliente(self):
        turno = self.txt_turno.text()
        if turno:
            mensaje = self.sistema_banco.agregarCliente(turno)
            self.lbl_agregar.setText(mensaje)
            self.lbl_agregar.setText("Turno agregado(turno): " + turno + " - Hora de entrada: " + datetime.now().strftime("%H:%M:%S"))
        else:
            self.lbl_agregar.setText("Ingrese un turno válido")
            self.actualizar_lbl_agregar()
            
            
    def atender_cliente(self):
        cliente_atendido, tiempo_espera = self.sistema_banco.atenderCliente()
        if cliente_atendido:
            mensaje = f"Cliente con turno {cliente_atendido['turno']} atendido. Tiempo de espera: {tiempo_espera:.2f} segundos"
            self.lbl_atender.setText(mensaje)
            tiempo_espera = datetime.now() - cliente_atendido["hora_entrada"]
            
            
            
        else:
            self.lbl_atender.setText("No hay clientes en espera")
            self.actualizar_lbl_atender()

    def cerrar_banco(self):
        # 1. Bloqueamos de inmediato el ingreso de nuevos turnos
        self.txt_turno.setEnabled(False)
        
        # 2. Contamos cuántos clientes quedan realmente en la cola enlazada
        clientes_restantes = 0
        temp = self.sistema_banco.cola.first
        while temp is not None:
            clientes_restantes += 1
            temp = temp.next
        
        # 3. Si todavía quedan clientes por atender
        if clientes_restantes > 0:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(
                self, 
                "Clientes pendientes", 
                f"No se puede cerrar por completo. Aún quedan {clientes_restantes} clientes en la cola. ¡Por favor, atiéndalos!"
            )
            # Nos aseguramos de mantener el botón de Atender activo
            self.btn_atender.setEnabled(True)
            self.lbl_atender.setText(f"Clientes en espera: {clientes_restantes}")
            
        # 4. Si ya no queda nadie, cerramos definitivamente el banco
        else:
            self.lbl_abierto.setText(self.sistema_banco.cerrarBanco())
            
            # Desactivamos los botones por completo
            self.btn_atender.setEnabled(False)
            self.btn_cerrar.setEnabled(False)
            self.lbl_atender.setText("")
            
            # Mostramos las estadísticas finales en la interfaz
            if self.sistema_banco.total_clientes == 0:
                self.lbl_clientes.setText("Total de clientes atendidos: " + str(0))
                self.lbl_tiempo.setText("Tiempo promedio: " + str(0) + "s")
            else:
                self.lbl_clientes.setText("Total de clientes atendidos: " + str(self.sistema_banco.total_clientes))
                self.lbl_tiempo.setText("Tiempo promedio: " + str(self.sistema_banco.promedio) + "s")
        
            
                
    
            
        

 