from estructuras.lineales.lista_enlazada_simple import LinkedList
from estructuras.lineales.queue import Queue
from estructuras.lineales.banco import MenuBanco

class MenuListaEnlazada(object):
        def __init__(self):
            self.lista_enlazada = LinkedList()
            self.queue = Queue()

        def mostrar_menu_principal(self):
            while True:
                seleccion = input("Seleccione una opción:(Menu lista enlazada (1), Menu cola (2), Menu banco (3)): ")
                if seleccion == "1":
                    self.mostrar_menu_lista_enlazada()
                elif seleccion == "2":
                    self.mostrar_menu_queue()
                elif seleccion == "3":
                    self.mostrar_menu_banco()
                elif seleccion == "4":
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción no válida")

        def mostrar_menu_lista_enlazada(self):
            while True:
                print("Menu de la lista enlazada")
                print("1. Insertar al principio")
                print("2. Insertar al final")
                print("3. Buscar")
                print("4. Imprimir")
                print("5. Eliminar al principio")
                print("6. Eliminar al final")
                print("7. Salir")
                
                opcion = input("Seleccione una opción: ")
                if opcion == "7":
                    break
                
                if opcion in ["1", "2", "3", "4", "5", "6"]:
                    self.ejecutar_opcion(int(opcion))
                else:
                    print("Opción no válida")

        def mostrar_menu_queue(self):
            while True:
                print("Menu de la cola")
                print("1. Encolar")
                print("2. Desencolar")
                print("3. Consultar primer elemento")
                print("4. Consultar último elemento")
                print("5. Imprimir")
                print("6. Salir")
                
                opcion = input("Seleccione una opción: ")
                if opcion == "6":
                    break
                    
                if opcion in ["1", "2", "3", "4", "5", "6"]:
                    self.ejecutar_opcion_cola(int(opcion))
                else:
                    print("Opción no válida")

        def ejecutar_opcion(self, opcion):
            if opcion == 1:
                elemento = input("Ingrese el elemento a insertar: ")
                self.lista_enlazada.insert_at_beginning(elemento)
                print(f"Elemento {elemento} agregado al principio de la lista")
            elif opcion == 2:
                elemento = input("Ingrese el elemento a insertar: ")
                self.lista_enlazada.insert_at_end(elemento)
                print(f"Elemento {elemento} agregado al final de la lista")
            elif opcion == 3:
                elemento = input("Ingrese el elemento a buscar: ")
                encontrado = self.lista_enlazada.search(elemento)
                if encontrado:
                    print(f"Elemento {elemento} encontrado")
                else:
                    print(f"Elemento {elemento} no encontrado")
            elif opcion == 4:
                print("Contenido de la Lista enlazada:")
                self.lista_enlazada.print_linked_list()
            elif opcion == 5:
                elemento = input("Ingrese el elemento a eliminar al principio: ")
                encontrado = self.lista_enlazada.search(elemento)
                if encontrado:
                    self.lista_enlazada.delete_at_beginning()
                    print(f"Elemento {elemento} eliminado")
            elif opcion == 6:
                elemento = input("Ingrese el elemento a eliminar al final: ")
                encontrado = self.lista_enlazada.search(elemento)
                if encontrado:
                    self.lista_enlazada.delete_at_end()
                    print(f"Elemento {elemento} eliminado")

        def ejecutar_opcion_cola(self, opcion):
            if opcion == 1:
                elemento = input("Ingrese el elemento a encolar: ")
                self.queue.enqueue(elemento)
                print(f"Elemento {elemento} encolado")
            elif opcion == 2:
                elemento = self.queue.dequeue()
                print(f"Elemento desencolado: {elemento}")
            elif opcion == 3:
                elemento = self.queue.firstQueue()
                print(f"Primer elemento: {elemento}")
            elif opcion == 4:
                elemento = self.queue.lastQueue()
                print(f"Último elemento: {elemento}")
            elif opcion == 5:
                elemento = self.queue.printQueue()
                print(f"Elementos en la cola: {elemento}")
        

        
    

    
    
    
        
    
    
    