Leetcode – preporučeni zadaci za vježbu
▪ Osnove
 20. Valid Parentheses — Easy
 155. Min Stack — Medium, stog koji pamti minimalni element!
 232. Implement Queue using Stacks — Easy
▪ Rad s monotonim stogom
 739. Daily Temperatures — Medium, koliko dana čekamo toplije?
 496. Next Greater Element I — Easy, klasična primjena monotenog stoga
▪ Osnove reda
 933. Number of Recent Calls — Easy
 225. Implement Stack using Queues — Easy


20. Valid Parentheses — Easy
class Solution(object):
    def isValid(self, s):
        stack = []

        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in bracket_map:
                if not stack or stack.pop() != bracket_map[i]:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0

155. Min Stack — Medium, stog koji pamti minimalni element!
class MinStack(object):
    

    def __init__(self):
        self.items = []
        

    def push(self, value):
        self.items.append(value)              
        """
        :type value: int
        :rtype: None
        """
        

    def pop(self):
        return self.items.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.items[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return min(self.items)
        """
        :rtype: int
        """
        
232. Implement Queue using Stacks — Easy ▪ Rad s monotonim stogom
class MyQueue(object):

    def __init__(self):
        self.items = []
        

    def push(self, x):
        return self.items.append(x)

        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if self.empty():
            raise IndexError("IsEmpty")
        else:
            return self.items.pop(0)
        """
        :rtype: int
        """
        

    def peek(self):
        if self.empty():
            raise IndexError("IsEmpty")
        else:
            return self.items[0]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.items) == 0
        """
        :rtype: bool
        """
