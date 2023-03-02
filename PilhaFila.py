class Pilha:
    def __init__(self):
        self.fila = []
        self.tamanho = 0
    def addGame(self, nomejogo):
        self.fila.append(nomejogo.lower())
        self.tamanho += 1
    def mostraritens(self):
        
        for i in self.fila:
            print(i)
           
           
            
    def mostrarquantidade(self):
        print(self.tamanho)
    
    def removerdoInicio(self, game):
        
        for j in self.fila:
             if game.lower() == j:
                 self.fila.remove(j)
                 self.fila.append(game.lower())
        
                
                 
        
        
    
    
        
    
            
    
fila = Pilha()

fila.addGame("God of War")
fila.addGame("Legend of Zelda")
fila.addGame("GTA 5")
fila.mostraritens()
fila.removerdoInicio("God of War")
fila.mostraritens()

    
    
