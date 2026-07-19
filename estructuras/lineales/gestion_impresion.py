from estructuras.lineales.queue import Queue, Node

class TrabajoImpresion:
    def __init__(self, usuario: str, documento: str, paginas: int, consecutivo: int):
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas
        self.consecutivo = consecutivo

    def __str__(self):
        return f"[{self.consecutivo}] {self.usuario} -> {self.documento} ({self.paginas} págs.)"


class GestorImpresion:
    def __init__(self, queue_instance):
        # Recibe la instancia de tu clase Queue por composición
        self.cola = queue_instance
        self._contador_consecutivo = 1
        self._total_elementos = 0  # Monitorea el tamaño de la cola enlazada

    def agregar_trabajo(self, usuario: str, documento: str, paginas: int) -> tuple[bool, str]:
        # Validaciones obligatorias
        if not usuario.strip() or not documento.strip():
            return False, "Error: El usuario y el documento no pueden estar vacíos."
        if paginas < 1:
            return False, "Error: El número de páginas debe ser mayor o igual a 1."
        
        # Crear el objeto y encolar
        nuevo_trabajo = TrabajoImpresion(usuario.strip(), documento.strip(), paginas, self._contador_consecutivo)
        self.cola.enqueue(nuevo_trabajo)  # Uso real de enqueue
        
        self._contador_consecutivo += 1
        self._total_elementos += 1
        return True, f"Trabajo '{nuevo_trabajo.documento}' agregado con éxito."

    def procesar_siguiente(self) -> tuple[bool, str]:
        if self.cola.is_empty():  # Uso real de is_empty para validar error
            return False, "Error: No hay trabajos pendientes en la cola de impresión."
        
        trabajo_atendido = self.cola.dequeue()  # Uso real de dequeue
        self._total_elementos -= 1
        return True, f"Imprimiendo: {trabajo_atendido}"

    def obtener_frente(self) -> str:
        if self.cola.is_empty():  # Uso real de is_empty
            return "Cola vacía"
        
        trabajo_frente = self.cola.firstQueue()  # Uso real de tu método firstQueue()
        return str(trabajo_frente)

    def obtener_total(self) -> int:
        return self._total_elementos

    def listar_trabajos(self) -> list:
        # Recorremos de manera segura los nodos de tu Queue para pasarlos a la interfaz
        lista_cadenas = []
        actual = self.cola.first  # Acceso al nodo inicial
        while actual is not None:
            lista_cadenas.append(str(actual.data))
            actual = actual.next
        return lista_cadenas
    
    def validar_e_imprimir(self) -> tuple[bool, str]:
        """Nueva función para validar de forma segura si la cola está vacía antes de imprimir."""
        if self.cola.is_empty():  # Uso real de tu método is_empty()
            return False, "Error: ¡No puedes imprimir porque la cola está completamente vacía!"
        
        # Si no está vacía, procede a desencolar
        trabajo_atendido = self.cola.dequeue()  
        self._total_elementos -= 1
        return True, f"Imprimiendo: {trabajo_atendido}"

    def validar_y_encolar(self, usuario: str, documento: str, paginas: int) -> tuple[bool, str]:
        """Nueva función para validar las páginas y campos vacíos antes de alterar la cola."""
        if not usuario.strip() or not documento.strip():
            return False, "Error: El usuario y el documento no pueden estar vacíos."
        
        if paginas < 1:
            # Si es 0 o negativo, frena el flujo aquí con un return
            return False, "Error: No se puede agregar un documento con 0 páginas. La cola no sufrió cambios."