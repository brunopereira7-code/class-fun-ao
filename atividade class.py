import os 
from dataclasses import dataclass 
os.system("cls")


@dataclass

class pessoa:
    nome:str
    idade:int
    peso:float
    altura:float


pessoa1=pessoa(nome=input("Digite seu nome:"), 
               idade=int(input("Digite sua idade")), 
               peso=float(input("Digite seu peso")),
               altura=float(input("Digite sua altura")))

print("Exibindo dados")
print(f"nome: {pessoa1.nome}")
print(f"idade: {pessoa1.idade}")
print(f"peso: {pessoa1.peso} KG")
print(f"altura: {pessoa1.altura}")