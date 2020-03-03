class Node(object):
    
    def __init__(self, data):
        
        self.data = data
        self.nextnode = None
        
        
class linkedlist(object):
    
    def __init__(self):
        self.rootnode = None
        self.size = 0
        
    def insert(self, data):

        newnode = Node(data)
        
        if not self.rootnode:
            self.rootnode = newnode
        else:
            newnode.nextnode = self.rootnode
            self.rootnode = newnode
        
    def getLast(self, value):
        position = self.rootnode
        farword = self.rootnode

        
        while self.size < (value-1):
            
            farword = farword.nextnode
            self.size +=1 
    
            
        while farword.nextnode == None:
            farword = farword.nextnode
            position = position.nextnode
            

        print(farword.data)
        
    
last = linkedlist()
last.insert("A")
last.insert("b")
last.insert("c")
last.insert("d")
last.insert("e")
last.insert("f")
last.getLast(4)
  
######### Output : c ######## from the last the n = 4 = c #########
