#!/usr/bin/python

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#    def __repr__(self):
#        #return repr(self.data)
#        return self.data

    def __str__(self):
        return str(self.data)

    def list_nodes(self):
        while self:
            print self.data
            self = self.next 

a = Node(1,Node(2,Node(3)))
print a
print a.next
print a.next.next

d = Node(7)
c = Node(6, d)
b = Node(5, c)
a.next.next.next = Node(4, b)

print a.next.next.next
print a.next.next.next.next
print a.next.next.next.next.next

# print a.next.next.next.next.next.next
print d


e = Node(8)
d = Node(7,e)

print "starting over"

a.list_nodes()
