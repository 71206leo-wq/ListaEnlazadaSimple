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
    
class EvaluadorPosfija:
    def __init__(self):
        # Usamos tu clase Stack existente para almacenar operandos numéricos
        self.pilaEvalua = Stack()

    def evaluar(self, expresion_posfija: str) -> float:
        # 1. Recorrer la expresión posfija de izquierda a derecha 
        for caracter in expresion_posfija:
            
            # Si es un espacio, lo ignoramos
            if caracter == ' ':
                continue
            # 2. Si el elemento es un operando (dígito), se convierte a número y se apila 
            if caracter.isdigit():
                self.pilaEvalua.push(int(caracter)) # Uso de push
                
            # 3. Si es un operador, se desapilan dos operandos y se aplica la operación 
            elif caracter in ['+', '-', '*', '/', '$']:
                # El primero en salir (pop) es el segundo operando 
                op2 = self.pilaEvalua.pop() 
                # El segundo en salir (pop) es el primer operando 
                op1 = self.pilaEvalua.pop() 
                
                # Evaluación manual sin usar eval() 
                if caracter == '+':
                    resultado = op1 + op2
                elif caracter == '-':
                    resultado = op1 - op2
                elif caracter == '*':
                    resultado = op1 * op2
                elif caracter == '$':
                    resultado = op1 ** op2
                elif caracter == '/':
                    resultado = op1 / op2
                
                # 4. Apilar el resultado parcial 
                self.pilaEvalua.push(resultado)
                
        # 5. Al finalizar, el único valor restante en la pila es el resultado definitivo 
        return self.pilaEvalua.pop()