"""
Faça um algoritmo que solicite ao usuário informar 2 números. Em seguida, some os valores e envie para a saída
padrão a seguinte frase: "A soma entre <X> e <Y> é igual <total>".
"""
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

soma =  num1+num2;
print("%d + %d = %d" %(num1,num2,soma))