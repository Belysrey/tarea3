class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

def my_stack_function(arr):
    stack = Stack()

    # Ordenar el arreglo de forma ascendente
    sorted_arr = sorted(arr)

    for num in sorted_arr:
        stack.push(num)

    return stack

# Ejemplo de uso:
arr = [1, 0, -2, -33, 10]
stack = my_stack_function(arr)

# Mostrar si la pila está vacía
print(stack.isEmpty())  # True

# Apilar el valor 100
stack.push(100)

# Apilar el valor 200
stack.push(200)

# Desapilar el valor 200
print(stack.pop())  # 200

# Validar el tamaño de la pila
print(stack.size())  # 5

# Mostrar el primer elemento de la pila
print(stack.top())  # 10

# Mostrar los elementos en la pila
print(stack.items)  # [-33, -2, 0, 1, 10, 100]
