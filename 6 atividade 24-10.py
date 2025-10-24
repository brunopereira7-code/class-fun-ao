import os
from dataclasses import dataclass

os.system("cls")
@dataclass

class Pessoa:
    nome:str
    idade:int
    peso:float
    altura:float

    def mostrar_resultado(self):
        print(f"seu nome é {self.nome}")
        print(f"sua idade {self.idade}")
        print(f"seu peso {self.peso}")
        print(f"sua altura é {self.altura}")

lista_de_cliente=[]

cliente=Pessoa(nome=input("digite seu nome"),
               idade=int(input("Digite sua idade")),
               peso=float(input("Digite seu peso")),
               altura=float(input("Digite sua altura")),
               ) 
lista_de_cliente.append(cliente) 


