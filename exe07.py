class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def escreve(self):
        print(self.nome,self.idade)
        
class Estudante(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.graduacao = 2024

x = Estudante ('Maria', 22)
x.escreve()
print("Eu me formo em " ,x.graduacao)

#super se refere a classe pessoa