import os 
from dataclasses import dataclass
os.system("cls")

@dataclass

class pessoas:
    nome:str
    email:str
    telefone:int
    endereço:str


pessoa1=pessoas(nome=input("Digite seu nome"), 
                email= input("digite seu e-mail"),
                telefone=int(input("Digite seu telefone")),
                endereço=input("Digite seu endereço"))
                

print("-----Exibindo Resultados-----")
print(f"nome é {pessoa1.nome}")
print(f"e-mail é {pessoa1.email}")
print(f"seu telefone é {pessoa1.telefone}")
print(f"endereço é {pessoa1.endereço}")