
from platform import node

from platform import node

from estructuras.lineales import nodo
from estructuras.lineales.nolineales.binary_tree import BinaryTree
from binarytree import Node 

def convertir_a_binarytree(nodo):
    if nodo is None:
        return None
    
    nuevo = Node(nodo.value)
    nuevo.left = convertir_a_binarytree(nodo.left)
    nuevo.right = convertir_a_binarytree(nodo.right)
    
    return nuevo

def mostrar_recorridos(arbol):
    print("\nRecorrido en preorden:")
    arbol.preorden()

    print("Recorrido en inorden:")
    arbol.inorden()

    print("Recorrido en inorden con paréntesis:")
    arbol.inorden_con_parentesis()

    print("Recorrido en postorden:")
    arbol.posorden()

    try:
        resultado = arbol.evaluar()
        print(f"\nResultado numérico: {resultado}")
    except ValueError as error:
        print(f"\nNo se pudo evaluar numéricamente: {error}")


if __name__ == "__main__":
    expresion = input("Ingresa una expresión postfija separada por espacios (usa $ para potencia): ").strip()
    arbol = BinaryTree()
    arbol.build_expression_tree(expresion)

    try:
        raiz = arbol.build_expression_tree(expresion)
        print(f"\nRaíz del árbol: {raiz.value}")
        mostrar_recorridos(arbol)
    except ValueError as error:
        print(f"Error: {error}")
        print("Verifica que la expresión postfija sea válida.")

arbol_grafico = convertir_a_binarytree(arbol.root)
print(arbol_grafico)
