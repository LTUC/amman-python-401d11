class Node:
  def __init__(self,value):
    self.value=value
    self.next=None


class Queue:
    def __init__(self):
        self.front = None # first node in th queue
        self.back=None    # last node in queue    

    def enqueue(self,value) :
        node = Node(value)
        if self.is_empty():
          self.back = node
          self.front = node
        #check if queue is empty:
        # TODO
        # if not :
        else:
          self.back.next= node
          self.back = node 

    def dequeue(self):
        #check if queue is empty:
       
      if self.is_empty():
        return "empty queue !"
        #if not:
      else:
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value
    
    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"   

    def is_empty(self):
       return True if not self.front else False
      
class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
        #check if the statck is empty or not 
        # if its empty :
        #TODO
        #IF NOT :
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        #check if the statck is empty :
        #TODO raise an exception
        #else:
        temp= self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        #TODO
        pass
    def is_empty(self):
        #TODO
        #check if stack is empty-> True 
        #if not -> False
        return True if not self.top else False