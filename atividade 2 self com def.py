import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class pessoas:
    nome:str
    email:str
    telefone:int
    endereço:str
    def mostrar_resultados(self):
        print("-----Exibindo Resultados-----")
        print(f"nome é {self.nome}")
        print(f"e-mail é {self.email}")
        print(f"seu telefone é {self.telefone}")
        print(f"endereço é {self.endereço}")

pessoa1=pessoas(nome=input("Digite seu nome"), 
                email= input("digite seu e-mail"),
                telefone=int(input("Digite seu telefone")),
                endereço=input("Digite seu endereço"))
                

pessoa1.mostrar_resultados()