#!/usr/bin/python


# @param x, an integer
# @return an integer
def push(self, x):

    if len(self.__inner_stack) == 0:
        self.__min = x
    else:
        if x < self.__min:
            t = self.__min - x
            self.__min = x
            x = x - t

    self.__inner_stack.append(x)
# @return nothing
def pop(self):
    num = self.__inner_stack.pop()
    if (num < self.__min):
        num = self.__min + self.__min - num
        self.__min = num

    return num

# @return an integer
def top(self):
    num = self.__inner_stack.pop() 
    self.__inner_stack.append(num)
    #if i code as : num = self.__inner_stack[-1], oj tell me memery out
    return max(num, self.__min)

# @return an integer
def getMin(self):
    return self.__min

def __init__(self):
    self.__min = None
    self.__inner_stack = []
