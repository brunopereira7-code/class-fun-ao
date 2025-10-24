import os
from dataclasses import dataclass

os.system("cls")
@dataclass

class endereco:
    logradouro: str
    numero: int

@dataclass
class cliente:
    nome: str
    endereco: endereco

cliente1 = cliente(nome = "Marta",
                   endereco=endereco (logradouro='Rua A', numero=23))
                

print("Mostrar dados do cliente")     
print(f"nome: {cliente1.nome}")     
print(f"Endereço: {cliente1.endereco.logradouro}")   