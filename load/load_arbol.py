import sys
from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,  QMessageBox, QGraphicsScene, QMainWindow
from PyQt5.QtGui import QFont, QPen, QBrush, QColor
from PyQt5.QtCore import Qt


# Importación de tu estructura de Pila
PROJECT_ROOT = Path(__file__).resolve().parents[3] if len(Path(__file__).resolve().parents) > 3 else Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from estructuras.lineales.stack import Stack
except ImportError:
    pass
    


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

    def preorden_str(self, node=None, first=True):
        if first: node = self.root
        if node is None: return ""
        return f"{node.value} {self.preorden_str(node.left, False)} {self.preorden_str(node.right, False)}".strip()

    def inorden_str(self, node=None, first=True):
        if first: node = self.root
        if node is None: return ""
        return f"{self.inorden_str(node.left, False)} {node.value} {self.inorden_str(node.right, False)}".strip()

    def posorden_str(self, node=None, first=True):
        if first: node = self.root
        if node is None: return ""
        return f"{self.posorden_str(node.left, False)} {self.posorden_str(node.right, False)} {node.value}".strip()

    def inorden_con_parentesis(self, node=None, first=True):
        if first: node = self.root
        if node is None: return ""
        if node.left is None and node.right is None: return str(node.value)
        izq = self.inorden_con_parentesis(node.left, False)
        der = self.inorden_con_parentesis(node.right, False)
        return f"({izq} {node.value} {der})"


class ExpressionTreeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Carga directa del archivo de Qt Designer
        uic.loadUi('ui/Arbol_exp.ui', self)

        self.tree = BinaryTree()
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)

        # Enlace del botón con la función
        self.btn_build.clicked.connect(self.process_expression)

    def process_expression(self):
        expression = self.txt_postfix.text().strip()
        if not expression:
            QMessageBox.warning(self, "Advertencia", "Ingresa una expresión postfija.")
            return

        try:
            self.tree.build_expression_tree(expression)

            # Obtener recorridos
            pre = self.tree.preorden_str()
            ino = self.tree.inorden_str()
            pos = self.tree.posorden_str()
            parentesis = self.tree.inorden_con_parentesis()
            
            # 3. EVALUACIÓN: Calcular el resultado numérico de la operación
            # <--- ¡AQUÍ SE AGREGA LA EVALUACIÓN! --->
            try:
                resultado_evaluacion = self.tree.evaluar()
            except Exception as eval_err:
                resultado_evaluacion = f"No se pudo evaluar ({eval_err})"

            # Mostrar resultados en pantalla
            res_text = (
                f"• Preorden:   {pre}\n"
                f"• Inorden:    {ino}\n"
                f"• Posorden:   {pos}\n"
                f"• Infija con Paréntesis: {parentesis}"
                f"----------------------------------------\n"
                f"• RESULTADO DE LA OPERACIÓN: {resultado_evaluacion}"
            )
            self.txt_results.setText(res_text)

            # Dibujar árbol visualmente
            self.draw_tree()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def draw_tree(self):
        self.scene.clear()
        if self.tree.root:
            self._draw_node(self.tree.root, 0, 0, 160)

    def _draw_node(self, node, x, y, dx):
        if node is None:
            return

        radius = 20

        # Conectar con hijo izquierdo
        if node.left:
            self.scene.addLine(x, y, x - dx, y + 60, QPen(Qt.black, 2))
            self._draw_node(node.left, x - dx, y + 60, dx / 2)

        # Conectar con hijo derecho
        if node.right:
            self.scene.addLine(x, y, x + dx, y + 60, QPen(Qt.black, 2))
            self._draw_node(node.right, x + dx, y + 60, dx / 2)

        # Dibujar nodo y texto
        self.scene.addEllipse(x - radius, y - radius, radius * 2, radius * 2, QPen(QColor("#2b5c8f"), 2), QBrush(QColor("#e8f1f5")))
        text = self.scene.addText(str(node.value))
        text.setFont(QFont("Arial", 10, QFont.Bold))
        rect = text.boundingRect()
        text.setPos(x - rect.width() / 2, y - rect.height() / 2)

