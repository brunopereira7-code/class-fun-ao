import os 
from dataclasses import dataclass


os.system("cls") 
@dataclass
class Pessoa:
    nome:str
    e_mail:str
    endereco:str
@dataclass
class Endereco:
    logradouro:str
    numero:int
    
    def mostrar_resultado(self):
        print(f"seu nome é {self.nome}")
        print(f"seu e-mail é  {self.e_mail}")
        print(f"seu endereço é {self.endereco}") 
        print(f"seu logradouro é {self.logradouro}")
        print(f"seu numero da cada é {self.numero}")

lista_cliente=[]

cliente=Pessoa (nome=input("Digite seu nome"),
                e_mail=input("Digite seu e-mail")
                endereco=Endereco("Digite seu endereço")logradouro=input("Digite seu logradouro")numero=input("digite o numero da sua casa"),
                ) 
lista_cliente.append(cliente) 

cliente.mostrar_resultado()






