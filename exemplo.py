class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        print("Construindo")   
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}.'

leticia = Pessoa("Leticia", 49, 24)

print(leticia)
