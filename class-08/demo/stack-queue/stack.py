class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

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
        pass

    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"    


if __name__ ==  "__main__":
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    print(stack_01)
    print(stack_01.top.value)
