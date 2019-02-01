from linkedList import listNode, LinkedList

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    print ll.printList()
    ll.swapNodes(1,6)
    print ' ---- '
    ll.printList()