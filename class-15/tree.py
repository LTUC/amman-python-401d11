from assets import Node,Queue,Stack
class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None
    # children = []


class Tree:
  def __init__(self):
    self.root=None

  def breadth_first(self):
    if not self.root:
      return self.root
      
    output = []
    queue = Queue()
    queue.enqueue(self.root)

    while not queue.is_empty():
      
      front = queue.dequeue()
      output.append(front.value)
      
      if front.left :
          queue.enqueue(front.left)
      if front.right :
          queue.enqueue(front.right)  
        
    return output

  def pre_order(self):
    
    def _walk(root):
      #root
      print(root.value)

      #left
      if root.left :
        _walk(root.left)
        
      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)

  def in_order(self):
    def _walk(root):
      
      #left
      if root.left :
        _walk(root.left)
        
      #root
      print(root.value)

      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    
      
    
    

if __name__ == "__main__":
  tree = Tree()
  tree.root= Tnode(10)
  tree.root.left=Tnode(20)
  tree.root.right = Tnode(50)
  tree.root.left.left = Tnode(30)
  tree.root.left.right = Tnode(40)
  tree.root.right.left = Tnode(60)
  Tnode(20).left=Tnode(30)
  # print(Tnode(20).left)
  # print(tree.breadth_first())
  tree.pre_order() 
  print("###############")
  tree.in_order()