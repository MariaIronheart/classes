class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def escreve(self):
        print(self.nome,self.idade)
        
class Estudante(Pessoa):
    def __init__(self, nome, idade, ano):
        super().__init__(nome,idade)
        self.graduacao = ano
    def bemVindo(self):
        print('Bem-vindo', self.nome, 'para a classe', self.graduacao)
    
x = Estudante ('Maria', 22, 2024)
x.bemVindo()
