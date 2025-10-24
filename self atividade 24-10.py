import os 
from dataclasses import dataclass
os.system("cls") 

@dataclass
class Cliente:
    nome:str
    endereco:str

    def mostrar_dados(self):
        print(f"nome {self.nome}")
        print(f"endereço {self.endereco}")

lista_de_cliente=[]


for i in range(2):

    cliente= Cliente(
        nome=input("Digite seu nome:"),
        endereco=input("Digite seu endereço"),
    ) 
    lista_de_cliente.append(cliente)
    os.system("cls")
print("-----Mostrando resultando")
for cliente in lista_de_cliente:
    
    cliente.mostrar_dados()



