"""""
 Faça um algoritmo que peça um número ao usuário e verifique se o mesmo é par ou então ímpar.

"""
num1 = int(input("Informe um número: "))

par = num1 % 2

if(par == 1):
    print("Impar")
else:
    print("par")
