# import os 
# os.system("cls") 

# nota1=int(input("Digite sua primeira nota"))
# nota2=int(input("Digite sua segunda nota")) 
# notas=[]


# for i in range(2):
#     nota=int(input(f"Digite sua {i+1} nota:"))
#     notas.append(nota) 
# media=sum(notas)/len(notas)
# if nota > 7:
#     print("Aprovado")

# elif nota < 7:
#     print("Reprovado") 
# else:
#     print("Recuperaçao")

 

# print(f"suas notas foram {notas} ")
# print(f"sua media é {media}")
# print("fim do programa")


import os 
import time
 


lista_notas=[] 


def limpa_tela():
    time.sleep(2)
    os.system("cls")

def calcular_media(lista_notas):
    resultado=sum(lista_notas)/ 3
    return resultado

def resultado_final(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
limpa_tela()

for i in range(3):
    while True:
        nota=float(input("Digite sua nota")) 
        if nota >= 0 and nota <=10:
            lista_notas.append(nota)
            break 

        else:
            print("nota invalida" )
            time.sleep(2) 


media=calcular_media(lista_notas)

print(f"media é {media:.2f}")
resultado_final(media)