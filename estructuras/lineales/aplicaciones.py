from estructuras.lineales.stack import Stack
class Aplicaciones:
    def __init__(self):
        # Creamos la instancia de tu pila dentro de la clase Aplicaciones
        self.stack = Stack()
        
        # Diccionario de precedencia de operadores
        self.precedence = {
            '+': 1, 
            '-': 1, 
            '*': 2, 
            '/': 2, 
            '^': 3
        }

    def _get_precedence(self, operator):
        """Método auxiliar interno para medir la prioridad."""
        return self.precedence.get(operator, 0)

    def convert_infix_to_postfix(self, infix_expression: str) -> str:
        """
        Método que realiza la conversión utilizando tu estructura de Stack.
        """
        postfix_result = []
        tokens = infix_expression.replace(" ", "")  # Limpiamos espacios

        for token in tokens:
            # 1. Si es letra o número (operando)
            if token.isalnum():
                postfix_result.append(token)
            
            # 2. Si es paréntesis de apertura
            elif token == '(':
                self.stack.push(token)
            
            # 3. Si es paréntesis de cierre
            elif token == ')':
                while not self.stack.is_empty() and self.stack.top_of_stack() != '(':
                    postfix_result.append(self.stack.pop())
                
                if not self.stack.is_empty() and self.stack.top_of_stack() == '(':
                    self.stack.pop() # Eliminamos el '(' de la pila
            
            # 4. Si es un operador (+, -, *, /, ^)
            else:
                while (not self.stack.is_empty() and 
                       self._get_precedence(self.stack.top_of_stack()) >= self._get_precedence(token)):
                    postfix_result.append(self.stack.pop())
                
                self.stack.push(token)

        # 5. Vaciar los operadores restantes
        while not self.stack.is_empty():
            postfix_result.append(self.stack.pop())

        return "".join(postfix_result)