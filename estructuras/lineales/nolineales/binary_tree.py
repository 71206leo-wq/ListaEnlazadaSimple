
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from ..stack import Stack
except ImportError:
    from estructuras.lineales.stack import Stack


class NodeTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeExpression:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def _tokenize_postfix_expression(self, postfix_expression):
        operators = {"+", "-", "*", "/", "^", "$"}
        expression = postfix_expression.strip()
        tokens = []
        i = 0

        while i < len(expression):
            char = expression[i]

            if char.isspace():
                i += 1
            elif char in operators:
                tokens.append(char)
                i += 1
            else:
                start = i
                while i < len(expression) and not expression[i].isspace() and expression[i] not in operators:
                    i += 1
                tokens.append(expression[start:i])

        return tokens

    def build_expression_tree(self, postfix_expression):
        stack = Stack()
        operators = {"+", "-", "*", "/", "^", "$"}

        tokens = self._tokenize_postfix_expression(postfix_expression)

        for token in tokens:
            if token in operators:
                right_child = stack.pop()
                left_child = stack.pop()

                if right_child is None or left_child is None:
                    raise ValueError("Expresión postfija inválida")

                node = NodeExpression(token)
                node.left = left_child
                node.right = right_child
                stack.push(node)
            else:
                stack.push(NodeExpression(token))

        if stack.is_empty():
            raise ValueError("La expresión está vacía")

        root = stack.pop()

        if not stack.is_empty():
            raise ValueError("Expresión postfija inválida")

        self.root = root
        return self.root

    def insertar(self, value):
        self.root = self._insertar(self.root, value)

    def _insertar(self, node, value):
        if node is None:
            return NodeTree(value)
        if value < node.value:
            node.left = self._insertar(node.left, value)
        elif value > node.value:
            node.right = self._insertar(node.right, value)
        else:
            print("El valor ya existe en el árbol.")
        return node

    def buscar(self, value):
        return self._buscar(self.root, value)

    def _buscar(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._buscar(node.left, value)
        return self._buscar(node.right, value)

    def preorden(self):
        self._preorden(self.root)
        print()

    def _preorden(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._preorden(node.left)
            self._preorden(node.right)

    def inorden(self):
        self._inorden(self.root)
        print()

    def _inorden(self, node):
        if node is not None:
            self._inorden(node.left)
            print(node.value, end=" ")
            self._inorden(node.right)

    def inorden_con_parentesis(self):
        resultado = self._inorden_con_parentesis(self.root)
        print(resultado)
        return resultado

    def _inorden_con_parentesis(self, node):
        if node is None:
            return ""
        if node.left is None and node.right is None:
            return str(node.value)
        izquierda = self._inorden_con_parentesis(node.left)
        derecha = self._inorden_con_parentesis(node.right)
        return f"({izquierda} {node.value} {derecha})"

    def evaluar(self):
        if self.root is None:
            raise ValueError("El árbol está vacío")
        return self._evaluar(self.root)

    def _evaluar(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            try:
                return int(node.value)
            except ValueError as exc:
                raise ValueError("Los operandos deben ser números enteros") from exc

        izquierda = self._evaluar(node.left)
        derecha = self._evaluar(node.right)

        if node.value == "+":
            return izquierda + derecha
        elif node.value == "-":
            return izquierda - derecha
        elif node.value == "*":
            return izquierda * derecha
        elif node.value == "/":
            return izquierda / derecha
        elif node.value == "^":
            return izquierda ** derecha
        elif node.value == "$":
            return izquierda ** derecha
        else:
            raise ValueError("Operador no soportado")

    def posorden(self):
        self._posorden(self.root)
        print()

    def _posorden(self, node):
        if node is not None:
            self._posorden(node.left)
            self._posorden(node.right)
            print(node.value, end=" ")