class Node:
    def __init__(self):
        self.tree = []
        self.last = len(self.tree) - 1
        
    def insertroot(self, root):
        self.tree.insert(0, root)
        
        
    def insertLeft(self, value):
        
        if len(self.tree) == 1:
            self.tree.append(value)
        if value > self.tree[0]:
            if len(self.tree) % 2 != 0:
                if len(self.tree) > 1:
                    
                    if self.tree[self.last] > self.tree[self.last - 1]:
                        
                         self.tree.append(value)
                            
                        
                    else:
                        print("insert on the Right")
                    
                     
            
    def insertRight(self, value):
        if len(self.tree) == 2:
            self.tree.append(value)
        if value > self.tree[0]:
            if len(self.tree) % 2 == 0:
                    if self.tree[self.last] < value:
                
                    
                
                     self.tree.append(value)
                     
                    
            
    
    def getLeftval(self):
        if len(self.tree) == 3:
            print(self.tree[1])
            
        elif len(self.tree) > 3:
            
            print(self.tree[1::2])
         
           
        else:
            print("there is no tree yet")
            
       
                 
    
    def getRightChild(self):
        if len(self.tree) == 3:
            print(self.tree[2])
        elif len(self.tree) > 3:
                 print(self.tree[2::2])   
        else:
            print(self.tree[2])
        
        
       
            
    
    def getRoot(self):
        if len(self.tree) > 0:
            print(self.tree[0])
           
        else:
             print("there is no tree yet")
             
tree = Node()
tree.insertroot(0)
tree.insertLeft(1)
tree.insertRight(2)
tree.insertLeft(3)
tree.insertRight(4)


tree.getRoot()
tree.getLeftval()
tree.getRightChild()
            
        
            
            
            
        
        
            
