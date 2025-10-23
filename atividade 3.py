import os 
from dataclasses import dataclass
os.system("cls") 

@dataclass
class Pessoa:
    nome:str
    idade:int

    def mostrar_resultado(self):
        print(f"nome {self.nome}")
        print(f"idade {self.idade}") 

print("solciitando os dados da pessoa")
pessoa1=Pessoa(nome=input("Digite seu nome"),
               idade=int(input("Digite sua idade")))


pessoa2=Pessoa(nome=input("Digite seu nome"),
               idade=int(input("Digite sua idade")))


print("------Exibindo resultado-----") 
pessoa1.mostrar_resultado()
pessoa2.mostrar_resultado()
