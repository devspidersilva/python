"""""
Faça um algoritmo que peça a idade de uma pessoa
 e imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.

"""
idade = float(input("Informe sua idade : "))


if(idade >=18 and idade <65):
    print("De maior")
elif(idade >=65 and idade<120):
    print("Idoso")
elif(idade>=1 and idade<18):
    print("de menor")
elif(idade>=0 and idade <1):
    print("bebê")
else:
    print("idade invalida")