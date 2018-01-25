"""
STACK WITH GET MINIMUM ELEMENT
"""

class MinStack(object):

    def __init__(self):
        self.items = []
        self.minstack = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, x):
        self.items.append(x)
        if self.minstack == []:
            self.minstack.append(x)
        elif self.minstack[-1] >= x:
            self.minstack.append(x)
        

    def pop(self):
        if self.minstack[-1] == self.items[-1]:
            if len(self.items) > 1:
                self.minstack = self.minstack[:-1]
            else:
                self.minstack = []
        return self.items.pop()
        

    def top(self):
        return self.items[-1]
        

    def getMin(self):
        if self.minstack == []:
            return None
        return self.minstack[-1]