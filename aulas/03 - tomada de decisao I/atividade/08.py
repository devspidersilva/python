"""""
 Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.

"""
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if(num1 == num2):
    print("Os dois números são iguais")
else:
    print (max(num1, num2))
    print(min(num1, num2))
