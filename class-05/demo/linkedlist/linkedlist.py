class Node : #value next
    def __init__(self, value,_next=None):
        self.value = value
        self.next = _next



class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def traverse(self) :
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def insert (self, value) : 
         # insert vs append 
         new_node = Node(value)
         new_node.next = self.head
         self.head = new_node

         






if __name__ == '__main__':

    node_d=Node ("duaa")
    node_H=Node ("Hussam",node_d)

    # print(node_d)

    # print(node_d.value)
    # print(node_d.next)
    # print(node_H)

    # print(node_H.value)
    # print(node_H.next.value)

    ll_ = LinkedList(node_H)
    # print(ll_.head.value)
    ll_.insert("Ibrahim")
    
    ll_.traverse()


