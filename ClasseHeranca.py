class Funcionario:
     def __init__(self, nome , salario, numeroId, senha):
         
         self._nome = nome
         self._salario = salario
         self._numeroId = numeroId
         self._senha = senha
         
     def autetication(self, senha):
        if self._senha == senha:
            print("Acesso Permitido")
        else:
            print("Acesso Negado")
     def bonific(self):
         return self._salario * 0.10
class Gerente(Funcionario):
    def __init__(self, nome, salario, numeroId, senha, qt_gerencidado):
        super().__init__(nome, salario, numeroId, senha )
        self.senha = senha
        
        self.qt_gerenciado = qt_gerencidado
        
    def bonificacao(self):
     return  super().bonific() + 1000 
 
 

gent  = Gerente("Ms", 1000, 1234, 48, 5)
gent.autetication(48) 

print(gent.bonificacao())
