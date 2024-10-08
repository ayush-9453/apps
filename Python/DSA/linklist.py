class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linklist:
    def __init__(self):
        self.head = None 

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head 
        while last.next is not None:
            last = last.next
        last.next = new_node

    def show(self):
        current = self.head
        while current:
            print(current.data,end='->')
            current = current.next
        print(None)
l = Linklist()
l.append(4)
l.append(5)
l.append(6)
l.show()
