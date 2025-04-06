from node import Node

class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
            self.size = 0
            return
        self.head = Node(data)
        self.size = 1

    def __repr__(self):
        if self.head is None:
            return "[]"
        
        result = "[" + str(self.head) + "]"
        return result
    
    #check size
    def length(self):
        return self.size

    def is_empty(self):
        if self.head is None:
            return True
        return False

    #insert nodes
    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

        self.size += 1

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.head
            current_node = self.head.next

            for i in range (1, index):
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = new_node
            new_node.next = current_node
        
        self.size += 1

    #change node value
    def set_at(self, index, data):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        current_node = self.head
        for i in range(0, index):
            current_node = current_node.next
        current_node.data = data

    #gets data and index
    def get_front(self):
        return self.head.data

    def contains(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def get_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current_node = self.head
        for i in range (0, index):
            current_node = current_node.next
        return current_node.data

    def index_of(self, data):
        current_node = self.head
        for i in range(0, self.size):
            if current_node.data == data:
                return i
            current_node = current_node.next
        return -1

    #delete nodes
    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.head
            current_node = self.head.next
            for i in range (1, index):
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = current_node.next
        self.size -= 1
    
    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            prev_node = self.head
            current_node = self.head.next
            while current_node:
                if current_node.data == data:
                    prev_node.next = current_node.next
                    self.size -= 1
                    return True
                prev_node = current_node
                current_node = current_node.next
        return False       
            