"""
Faça um algoritmo que solicite ao usuário digitar 2 números. Em seguida, imprima
o total decimal da divisão e o total inteiro (sem casas decimais):
"""
num1 = int(input("Informe um valor: "))
num2 = int(input("Informe outro valor: "))

div_decimal = num1/num2
div_int = num1//num2;
print("divisão float: %f \n divisão inteira: %d" %(div_decimal, div_int))