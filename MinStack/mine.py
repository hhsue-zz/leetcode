#!/usr/bin/python

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Hide Tags
'''

# [9,5,3,4,7,3]
# [9,5,3,3]

# reset min element always
# use a list to keep order of list 
# push = append. pop = pop. top = l[len(l)-1]. getMin = return self.__min

class MinStack:
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.__inner_stack.append(x)
        
    # @return nothing
    def pop(self):
        self.__inner_stack.pop()

    # @return an integer
    def top(self):
        return self.__inner_stack[len(__inner_stack)-1] 

    # @return an integer
    def getMin(self):
        return self.__ 

    # initialize
    def __init__(self):
        self.__min_stack = []
        self.__inner_stack = []
