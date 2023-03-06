class Aluno:
    def __init__(self):
         
         self.list = []
         self.contagem = 0
         self.index = []
    
    def addaluno(self, name):
        
         self.list.append(name.lower())
         self.contagem += 1
         print("adicionado")
         print(self.list)
         
    def getcontagem(self):
         print(self.contagem)
    
    def getlist(self):
         print(self.list)
    
    def removeAluno(self, name):
        
        try:
             metade = len(self.list) // 2
            
             if name.lower() in self.list[:metade]:
                
                 for i in range(len(self.list[:metade])):
                    if self.list[i] == name.lower():
                        
                        self.index.append(i)
                        
             if name.lower() in self.list[metade:]:
                 
                 for j in range( metade , len(self.list)):
                    
                     if self.list[j] == name.lower():
                        self.index.append(j)
                        
             for k in self.index:
                 self.list.pop(k)
             
             print("Removido Com Sucesso")
                
                
                
        except:
             print("Not Found on registers")
             print(self.list)
            

novoAluno = Aluno()
novoAluno.addaluno("Martim")
novoAluno.addaluno("Anir")
novoAluno.addaluno("Diniz")
novoAluno.addaluno("Safira")
novoAluno.getcontagem()
novoAluno.removeAluno("Safira")
novoAluno.getlist()
