numero1 = input("Digite o primeiro numero: ")
numero1 = int(numero1)

numero2 = input("Digite o segundo número: ")
numero2 = int(numero2)

if(numero1 == numero2):
    print("O número %d é igual a %d." %(numero1, numero2))
elif(numero1 != numero2):
    print("O número %d é diferente a %d." % (numero1, numero2))
elif(numero1 < numero2):
    print("O número %d é menor que %d." % (numero1, numero2))
elif (numero1 > numero2):
    print("O número %d é maior que %d." % (numero1, numero2))
elif (numero1 >= numero2):
    print("O número %d é maior ou igual a %d." % (numero1, numero2))
elif (numero1 <= numero2):
    print("O número %d é menor ou igual a %d." % (numero1, numero2))