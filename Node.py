class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.Next = None
        self.privious = None

    # set data of the node
    def setData(self, data):
        self.data = data
        #return self.data

    # get data of the node
    def getData(self):
        return self.data

    # set next of the node
    def setNext(self, next):
        #return self.Next
        self.Next = next

    # get next of the node
    def getNext(self):
        return self.Next

    # set previous of the node
    def setprevious(self, data):
        self.data = data
        #return self.data

    # get previous of the node
    def getprevious(self):
        return self.data


