import os 
from dataclasses import dataclass
os.system("cls") 

@dataclass
class informacoes:
    nome:str
    e_mail:str
    endereco:str


    def dados_da_entrega(self):
        print(f"nome {self.nome}")
        print(f"endereço {self.endereco}")



    def mostrar_dados(self):
        print(f"nome {self.nome}")
        print(f"e-mail: {self.e_mail}")
        print(f"endereço: {self.endereco}")



pessoa1=informacoes(nome=input("digite seu nome"), 
                    e_mail=input("Digite seu email:"), 
                    endereco=input("Digite seu endereço"))



# pessoa1 = informacoes(
#     # Correção: .strip().lower() vêm antes da vírgula
# nome=input("Digite seu nome: ").strip().lower(),
    
#     # Correção: Removido o espaço antes de .lower()
# e_mail=input("Digite seu e-mail: ").strip().lower(),
    
#     # Esta linha já estava correta!
# endereco=input("Digite seu endereço: ").strip().lower()
# )   


    
print("-----Seus dados--------")
pessoa1.mostrar_dados()

print("\n dados da entrega")
pessoa1.dados_da_entrega()