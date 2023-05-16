# LL: (1) -> (3) -> (2) -> None
#             ^
# 3, 5 Before the 3, insert the 5
# LL: (1) -> (5) -> (3) -> (2) -> (3)-> None


def insert_before_01(self,val_before, new_val):
    if self.head.value==val_before:
        node = Node(5,self.head)
        # node.next = self.head
        self.head = node 
        # self.insert(new_val)
        
    current = self.head
    
    while current.next is not None :
        if current.next.value == val_before:
            node = Node(new_val,current.next)
            # temp= current.next 
            current.next == node
            # node.next = temp 
            break 
        current=current.next
        

#####second method######
def insert_before_02(self, value_before, node_to_add):
    current = self.head # This assigns the current value to the head node
    while current:
        if current.value == value_before:
            node = Node(node_to_add, current)
            previous.next = node
            break

        previous = current
        current = current.next
