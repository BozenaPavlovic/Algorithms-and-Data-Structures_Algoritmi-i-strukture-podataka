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


739. Daily Temperatures — Medium, koliko dana čekamo toplije?
class Solution(object):
    def dailyTemperatures(self, temperatures):

        result = [0] * len(temperatures)  # answer for each day
        stack = []                        # indices waiting for warmer day

        for i in range(len(temperatures)):

            # warmer temperature found
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous = stack.pop()
                result[previous] = i - previous  # days waited

            stack.append(i)  # current day waits

        return result
        
496. Next Greater Element I — Easy, klasična primjena monotenog stoga
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []       # elementi koji još čekaju veći element
        greater = {}     # sprema: broj -> njegov sljedeći veći broj

        # prvo prolazimo kroz nums2 jer se tu traže odgovori
        for i in nums2:

            # ako je trenutni broj veći od zadnjeg u stogu
            while stack and i > stack[-1]:

                previous = stack.pop()       # uzimamo broj koji je čekao
                greater[previous] = i        # pronašli smo njegov veći broj

            stack.append(i)                  # trenutni broj čeka svoj veći broj

        # brojevi koji su ostali u stogu nemaju veći broj
        while stack:
            previous = stack.pop()
            greater[previous] = -1

        result = []

        # sada za nums1 samo dohvaćamo odgovore iz dictionaryja
        for i in nums1:
            result.append(greater[i])

        return result
        
933. Number of Recent Calls — Easy
class RecentCounter(object):

    def __init__(self):
        self.requests = []  # spremamo vremena svih dosad pristiglih zahtjeva

    def ping(self, t):
        self.requests.append(t)  # dodajemo novi zahtjev u red

        # t - 3000 je najstarije vrijeme koje još smije biti uključeno
        # sve što je manje od toga je prestaro
        while self.requests[0] < t - 3000:
            self.requests.pop(0)  # izbacujemo najstariji zahtjev

        # nakon izbacivanja ostaju samo zahtjevi unutar [t-3000, t]
        return len(self.requests)
        
225. Implement Stack using Queues — Easy
class MyStack(object):

    def __init__(self):
        self.q1 = []  # glavni queue, čuva elemente stacka
        self.q2 = []  # pomoćni queue

    def push(self, x):
        self.q2.append(x)  # novi element prvo ide u pomoćni queue

        # prebacujemo stare elemente iza novog
        while self.q1:
            self.q2.append(self.q1.pop(0))

        # zamijenimo queueove
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        # prvi element q1 je vrh stacka
        return self.q1.pop(0)

    def top(self):
        # samo pogledamo vrh bez uklanjanja
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0
        
