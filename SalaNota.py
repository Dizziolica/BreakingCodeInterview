class Aluno():
    def __init__(self):
        self.lista = []
        self.name = ""
        self.sobrenome = ""
        self.dictionary1 = {}
        
      
        
                 
    
    def inscricao(self, name, sobrenome):
        
        self.name = name
        self.sobrenome = sobrenome
        nomecompleto = self.name + "" + self.sobrenome
    
        self.lista.append(nomecompleto)
        
    def mostrarTurma(self):
        print(self.lista)  
        
        
    
    def  getNota(self, name, sobrenome, nota):
        
        dictionar = {self.name + "" + self.sobrenome: nota}
        self.dictionary1.update(dictionar)
        
    def aprovadoOrNot(self):
        if self.dictionary1[self.name + "" + self.sobrenome] > 15:
            print("Approved")
        
        else:
            print("not Approved")
                          
novoAluno = Aluno()
novoAluno.inscricao("Isis", "Biasoli")
novoAluno.inscricao("Safira", "Biasoli")
novoAluno.getNota("Isis", "Biasoli", 18)
novoAluno.aprovadoOrNot()



print(novoAluno.mostrarTurma())
