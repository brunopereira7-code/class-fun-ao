import os 
from dataclasses import dataclass
os.system("cls") 

@dataclass
class Pessoa:
    nome:str
    idade:int
    cpf=str

@dataclass
class Pet:
    nome:str 
    idade:int
    peso:float



pessoa1=Pessoa(nome= "Alice", cpf='323232323', idade= 30)
pet1=Pet ("bobinho", idade= 5, peso=2.100) 



# cpf_pessoa=int(input("Digite seu cpf:"))
# peso_pet=float(input("Digite o peso do  seu pet"))

print(f"Nome: {pessoa1.idade}, idade: {pessoa1.idade}  cpf: {pessoa1.cpf}")

print(f"Nome: {pet1.nome}, idade: {pet1.idade} peso: {pet1.peso}")