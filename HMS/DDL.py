class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DDL:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, patient): # patient is Patient class object
        newNode = Node(patient)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def dequeue(self, id): # id is integer value
        if self.head is None:
            return
        if(self.head.data.id == id):
            temp = self.head
            self.head = self.head.next
            del temp
            if self.head == None:
                return
            self.head.prev = None
            return
        temp = self.head.next
        while temp != None:
            if id == temp.data.id:
                temp.prev.next = temp.next
                if temp.next != None:
                    temp.next.prev = temp.prev
                del temp
                return
            temp = temp.next
        
        
    def display(self):
        temp = self.head
        while temp != None:
            print("{} {}".format(temp.data.name, temp.data.id))
            temp = temp.next
    
                    
                    