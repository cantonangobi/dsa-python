class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        result = "(Data: " + str(self.data) + ", Next -> " + str(self.next) + ")"
        return result