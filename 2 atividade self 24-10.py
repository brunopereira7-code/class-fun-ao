import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoas:
    nome:str
    cpf:str
    telefone:str
    telefone_marketing="71235689787"

    def mostrar_resultado(self):
        print(f"nome é {self.nome}")
        print(f"cpf é {self.cpf}")
        print(f"telefone é {self.telefone}") 

    def dados_marketing(self):
        print(f"telefone do marketing{self.telefone_marketing}") 


lista_de_cliente=[]

for i in range(3):
    cliente=Pessoas(
        nome=input("Digite seu nome"),
        cpf=input("Digite seu cpf"),
        telefone=input("Digite seu telefone")
    )
    lista_de_cliente.append(cliente)
    os.system("cls") 
for cliente in lista_de_cliente:
    print("--------Mostrando resultado----------")
    cliente.mostrar_resultado()
    cliente.dados_marketing()
    # cliente.mostrar_resultado(3)
    # resultado_marketing=(self,telefone_marketing)
    # dados_marketing(resultado_marketing)