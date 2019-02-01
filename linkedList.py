# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Singly Linked list datastructure implementation
# Author: Abinash Mohanty
# Date: 08/10/2017
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class listNode:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        """
        Print all the elements in the list.
        """
        tmp = self.head
        myStr = ''
        while(tmp):
            print tmp.data
            tmp = tmp.next

    def push(self, data):
        """
        Insert a node at the start of the linked list.
        """
        newNode = listNode(data)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self, prev, data):
        """
        Insert a node after a given node.
        """
        if prev is None:
            print 'Node should be a part of the list'
            return

        newNode = listNode(data)
        newNode.next = prev.next
        prev.next = newNode

    def append(self, data):
        """
        Insert a node at the end of the list.
        """
        newNode = listNode(data)
        if self.head is None:
            self.head = newNode
        last = self.head
        while(last.next):
            last = last.next
        last.next = newNode

    def deleteNode(self, key):
        """
        Delete the first occurance node with the given key
        """
        tmp = self.head
        if (tmp is not None) and (self.head.data == key):
            self.head = tmp.next
            tmp = None
            return
        while tmp is not None:
            if tmp.data == key:
                break
            prev = tmp
            tmp = tmp.next
        if tmp == None:
            return
        prev.next = tmp.next
        tmp = None

    def deleteNode_position(self, position):
        if self.head == None:
            return
        tmp = self.head
        if position == 0:
            self.head = tmp.next
            tmp = None
        for i in range(position-1):
            tmp = tmp.next
            if tmp == None:
                break
        if (tmp == None) or (tmp.next == None):
            return
        next = tmp.next.next
        tmp.next = None
        tmp.next = next

    def getCount_iterative(self):
        count = 0
        tmp = self.head
        while(tmp):
            count += 1
            tmp = tmp.next
        return count

    def getCount_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.getCount_recursive(node.next)

    def getCount(self):
        tmp = self.head
        n = self.getCount_recursive(tmp)
        return n

    def search(self, key):
        tmp = self.head
        while (tmp):
            if tmp.data == key:
                return True
            tmp = tmp.next
        return False

    def swapNodes(self, X, Y):
        if X == Y:
            return # Do nothing
        #find x and y
        currX = self.head
        prevX = None
        while(currX != None and currX.data != X):
            prevX = currX
            currX = currX.next

        currY = self.head
        prevY = None
        while(currY != None and currY.data != Y):
            prevY = currY
            currY = currY.next

        #check if X and Y exist in the list
        if currX == None or currY == None:
            return  # Do nothing

        if prevX == None:
            self.head = currY
        else:
            prevX.next = currY

        if prevY == None:
            self.head = currX
        else:
            prevY.next = currX

        tmp = currX.next
        currX.next = currY.next
        currY.next = tmp

    def getNthNode(self, N):
        tmp = self.head
        count = N


