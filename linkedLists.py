from Node import Node

class linkedLists:
    def __init__(self):
        self.head = None
        self.length = 1


    def printDList(self):
        if self.head is None:
            print(" Empty Doubly Linked List!!")
        else:
            current = self.head
            while current is not None:
                print(current.getData())
                current = current.getNext()


    def printDList_reverse(self):
        if self.head is None:
           print("Linked list is empty")
        else:
            current = self.head
            while current.getNext() is not None:
                print(current.getData())
                current = current.getNext()
            while current is not None:
                print(current.getData())
                current = current.getprevious()

    def listLength(self):
        current = self.head
        count = 0
        while current is not None:
            count = count +- 1
            current = current.getNext()
        return count


    def addNodeFirst(self, data):
        # create a noe node
        newNode = Node()
        newNode.setData(data)

        # Add to the beginning
        if self.head is None:
            self.head = newNode
        else:
            newNode.setNext = self.head
            self.head.setprevious (newNode)
            self.head = newNode
        self.length += 1

    def addNodeLast(self, data):
        # create a new node
        newNode = Node()
        newNode.setData(data)

        # add to the end
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() is not None:
                # Loop beakes
                current = current.getNext()
            current.setNext(newNode)
            newNode.setprevious  = current
        self.length += 1

    def addNodeInPos(self, pos, data):
        if pos > self.length -1 or pos < 0:
            return None
        elif pos == 0:
            self.addNodeFirst(data)
        elif pos == self.length - 1:
            self.addNodeLast(data)
        else:
            # creating the new Node
            newNode = Node()
            newNode.setData(data)
            count = 0
            current = self.head

            while count == pos - 1:
                count += 1
                current = current.getNext()
            newNode.setNext(current.getNext())
            current.setNext(newNode)
        self.length += 1

    def deleteBeginNode(self):
        if self.head is None:
            print("DLL is empty can't delete ! ")
            return

        if self.head.getNext() is None:
            self.head = None
            print("DLL is empty after deleting the Node ! ")
        else:
            self.head = self.head.getNext()
            self.head.getprevious = None
        self.length += 1

    def deleteEndNode(self):
        if self.head is None:
            print("DLL is empty can't delete")
            return

        if self.head.getNext() is None:
            self.head = None
            print("DLL is empty after deleting the node")

        else:
            current = self.head
            self.previous = None
            while current.getNext() is not None:
                self.previous = current
                current = current.getNext()
            self.previous.setNext(None)
        self.length -= 1












