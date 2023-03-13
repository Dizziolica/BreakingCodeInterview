class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limit):
        print("inicializando uma conta")
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limit = limit
    
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    def transfer_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.saldo += valor
            return True
        
    def extrato(self):
        print("numero: {} \nsaldo: {} ".format( self.numero, self.saldo))
        
cliente = Cliente("Homer", "Simpson", 123344)
conta = Conta(123, cliente , 1000, 500)
print(conta.saldo)
conta.deposita(200)
conta.extrato()

print(conta.titular.nome)
    
    
