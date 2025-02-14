def removeNthFromEnd(self, head, n):

    p1 = p2 = head
    for i in range(n):
        p1 = p1.next

    ## Delete the head node
    if p1 == None:
        return head.next

    while(p1.next != None):
        p1 = p1.next
        p2 = p2.next
    ## Delete the node
    if n == 1: # If delete the last node, set the last node is None
        p2.next = None
    else:
        p2.next = p2.next.next

    return head