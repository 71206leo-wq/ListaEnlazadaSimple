# Sistema de Simulación de Cola de Impresión

Este módulo simula la gestión de trabajos de impresión utilizando una estructura de datos lineal de tipo **Cola (Queue)** implementada mediante **Nodos Enlazados**. El flujo de los datos sigue estrictamente el principio **FIFO** (First In, First Out), asegurando que los documentos se procesen en el orden exacto en el que fueron enviados por los usuarios.

---

## 1. Descripción del Algoritmo

El sistema se basa en un modelo productor-consumidor controlado por la interfaz gráfica (`Qt Designer`):

1. **Captura y Validación**: El usuario ingresa los datos mediante un formulario (`QLineEdit` y `QSpinBox`). 
2. **Control de Restricciones**: Antes de alterar la estructura, el sistema verifica que los campos de texto no estén vacíos y que el número de páginas sea mayor o igual a 1. Si los datos son inválidos, el algoritmo aborta la operación emitiendo un mensaje de error y manteniendo la cola intacta.
3. **Asignación de Consecutivo**: Cada trabajo aprobado recibe un número identificador único e incremental (`consecutivo`), garantizando el rastreo de su turno en el sistema.
4. **Desencolado Seguro**: Al solicitar la impresión, el algoritmo verifica si existen nodos disponibles en la estructura enlazada. Si no hay elementos, bloquea la acción para evitar excepciones por punteros nulos (`None`).

---

## 2. Uso y Mapeo de la Estructura `Queue`

La lógica de negocio se comunica con la clase `Queue` existente mediante composición, aplicando sus operaciones fundamentales de la siguiente manera:

* **`enqueue(data)`**: Se utiliza al presionar el botón **"Agregar a la cola"**. Recibe un objeto de la clase `TrabajoImpresion` y crea un nuevo nodo al final (`self.last`) de la estructura enlazada.
* **`dequeue()`**: Se invoca a través del botón **"Imprimir siguiente"**. Desconecta el nodo ubicado al frente (`self.first`) de la cola, avanza el apuntador al siguiente elemento en línea y retorna la información del trabajo procesado.
* **`firstQueue()`**: Mapea la funcionalidad de un método *Front* o *Peek*. Se usa de forma automática para reflejar en tiempo real qué trabajo está esperando al inicio de la fila, sin llegar a extraerlo o eliminarlo de la cola.
* **`is_empty()`**: Operación de control crítico. Se ejecuta obligatoriamente antes de invocar a `dequeue()` o `firstQueue()`. Si el apuntador `self.first` es `None`, detiene el flujo informando al usuario que la cola está vacía, previniendo así un error de tipo `AttributeError`.
* **Monitoreo de Tamaño (`size`)**: Al ser una estructura de nodos dinámicos sin contador interno en la clase `Queue` base, el gestor mantiene un registro numérico (`self._total_elementos`) que incrementa unitariamente con cada `enqueue()` válido y disminuye con cada `dequeue()` exitoso, desplegando el total en la interfaz.

---

## 3. Estructura de Clases Implementada

* **`TrabajoImpresion`**: Clase entidad encargada de moldear los atributos solicitados (usuario, documento, páginas y consecutivo).
* **`GestorImpresion`**: Clase controladora que encapsula la instancia de la `Queue` y expone las funciones de validación (`validar_y_encolar` y `validar_e_imprimir`) hacia los eventos de la interfaz gráfica de Qt.