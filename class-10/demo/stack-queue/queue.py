class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    

    def  enqueue(self,value) :
        node = Node(value)
        #check if queue is empty:
        # TODO
        # if not :
        
        self.back.next= node
        self.back = node 

    def dequeue(self):
        #check if queue is empty:
        # TODO
        #if not:
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


if __name__ == "__main__":
    q=Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    print(q)
    print(q.front.value)
    print(q.back.value)
    print("deleted element is ",q.dequeue())#deleted node value
    print(q)






