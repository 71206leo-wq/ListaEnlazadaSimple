from estructuras.lineales.nolineales.binary_tree import BinaryTree


def verificar(expresion):
    arbol = BinaryTree()
    raiz = arbol.build_expression_tree(expresion)
    print(f"Expresión: {expresion}")
    print(f"Raíz: {raiz.value}")
    print(f"Hijo izquierdo: {raiz.left.value if raiz.left is not None else None}")
    print(f"Hijo derecho: {raiz.right.value if raiz.right is not None else None}")
    print()


if __name__ == "__main__":
    verificar("a b +")
    verificar("a b c + *")
    verificar("a b $")
    verificar("a b c + d * +")
