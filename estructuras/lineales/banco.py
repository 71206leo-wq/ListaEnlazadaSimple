import time
from datetime import datetime
from estructuras.lineales.queue import Queue
from estructuras.lineales.nodo import Node

class Banco:
    def __init__(self):
        self.cola = Queue()
        self.turnos = set()  # Conjunto para almacenar los turnos existentes
        self.abierto = True
        self.total_clientes = 0
        self.tiempo_total_espera = 0.0

    def agregarCliente(self, turno):
        if turno in self.turnos:
            return "Ya hay un cliente con ese turno"
        else:
            hora_entrada = datetime.now()
            cliente = {"turno": turno, "hora_entrada": hora_entrada}
            self.cola.enqueue(cliente)
            self.turnos.add(turno)
            return f"Turno {turno} agregado a la cola"

    def atenderCliente(self):
        if not self.cola.is_empty():
            cliente_atendido = self.cola.dequeue()
            self.turnos.remove(cliente_atendido["turno"])
            tiempo_espera = (datetime.now() - cliente_atendido["hora_entrada"]).total_seconds()
            self.total_clientes += 1
            self.tiempo_total_espera += tiempo_espera
            return cliente_atendido, tiempo_espera
        else:
            return None, 0.0

    @property
    def promedio(self):
        if self.total_clientes == 0:
            return 0.0
        else:
            return self.tiempo_total_espera / self.total_clientes

    def cerrarBanco(self):
        if not self.abierto:
            return "El banco ya está cerrado"
        else:
            self.abierto = False
            return "El banco ha sido cerrado"
