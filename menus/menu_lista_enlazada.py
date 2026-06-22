from estructuras.lineales.lista_enlazada_simple import LinkedList
class MenuListaEnlazada(object):
    def __init__(self):
        self.lista_enlazada = LinkedList()
        
    def mostrar_menu(self):
        print("Menu de la lista enlazada")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Buscar")
        print("4. Imprimir")
        print("5. Eliminar al principio")
        print("6. Eliminar al final")
        print("7. Salir")
        
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
        elif opcion == 7:
            print("Saliendo...")
            exit()
            
    def iniciar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 7:
                    self.ejecutar_opcion(opcion)
                    break
                self.ejecutar_opcion(opcion)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
            
        
        
        
        
    
        
    

    
    
    
        
    
    
    