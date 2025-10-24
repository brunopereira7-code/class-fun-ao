import os
from dataclasses import dataclass

os.system("cls")  # limpa tela no Windows

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    e_mail: str
    endereco: Endereco

    def mostrar_resultado(self):
        print(f"\nSeu nome é: {self.nome}")
        print(f"Seu e-mail é: {self.e_mail}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número da casa: {self.endereco.numero}")


# lista de clientes
lista_cliente = []

# entrada de dados
nome = input("Digite seu nome: ")
e_mail = input("Digite seu e-mail: ")
logradouro = input("Digite seu logradouro: ")
numero = int(input("Digite o número da sua casa: "))

# cria o objeto Endereco e Pessoa
endereco = Endereco(logradouro=logradouro, numero=numero)
cliente = Pessoa(nome=nome, e_mail=e_mail, endereco=endereco)

# adiciona à lista
lista_cliente.append(cliente)

# exibe resultado
cliente.mostrar_resultado()
