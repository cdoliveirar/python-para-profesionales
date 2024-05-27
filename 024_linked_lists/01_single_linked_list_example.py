'''
Una lista enlazada es una colección de nodos, cada uno compuesto por una referencia y un valor. Los nodos se unen en
una secuencia utilizando sus referencias. Las listas enlazadas pueden usarse para implementar estructuras de datos
más complejas como listas, pilas, colas y arreglos asociativos.
'''

''' Este ejemplo implementa una lista enlazada con muchos de los mismos métodos que el objeto lista incorporado. '''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Verifica si la lista está vacía"""
        return self.head is None

    def add(self, item):
        """Añade el elemento a la lista"""
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def size(self):
        """Devuelve la longitud/tamaño de la lista"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """Busca el elemento en la lista. Si se encuentra, devuelve True. Si no se encuentra, devuelve False"""
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """Elimina el elemento de la lista. Si el elemento no se encuentra en la lista, lanza un ValueError"""
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError
            print('Value not found.')

    def insert(self, position, item):
        """
        Inserta el elemento en la posición especificada.
        Si la posición especificada está fuera de los límites, lanza un IndexError
        """

        if position > self.size() - 1:
            raise IndexError
            print("Index out of bounds.")
        current = self.head
        previous = None
        pos = 0
        if position is None:
            self.add(item)
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)

    def index(self, item):
        """
       Devuelve el índice donde se encuentra el elemento.
       Si el elemento no se encuentra, devuelve None
        """
        current = self.head
        pos = 0
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position=None):
        """
        Si no se proporciona un argumento, devuelve y elimina el elemento en la cabeza.
        Si se proporciona una posición, devuelve y elimina el elemento en esa posición.
        Si el índice está fuera de los límites, lanza un IndexError.
        """

        if position > self.size():
            print('Index out of bounds')
            raise IndexError
        current = self.head
        if position is None:
            ret = current.getData()
            self.head = current.getNext()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.getNext()
                pos += 1
                ret = current.getData()
            previous.setNext(current.getNext())
        print(ret)
        return ret


    def append(self, item):
        """Añadir un elemento al final de la lista"""
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.getNext()
            pos += 1
        new_node = Node(item)
        if previous is None:
            new_node.setNext(current)
            self.head = new_node
        else:
            previous.setNext(new_node)

    def printList(self):
        """Imprime la lista"""
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()


ll = LinkedList()
ll.add('l')
ll.add('H')
ll.insert(1,'e')
ll.append('l')
ll.append('o')
ll.printList()