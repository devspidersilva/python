"""""
Faça um algoritmo que peça a idade do usuário
e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve.

"""
idade = float(input("Informe sua idade : "))
idade2 = float(input("Informe a idade de sua mãe: "))

if(idade2-idade >= 13):
    parto = idade2 - idade
    print("sua mãe o teve com %d anos de idade"%(parto))
else:
    print("idade da sua mãe está incorreta ou está muito nova")