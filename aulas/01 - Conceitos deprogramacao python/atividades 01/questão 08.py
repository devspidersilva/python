"""
Faça um algoritmo que solicite ao usuário informar 2 números. Em seguida, some os valores e envie para a saída
padrão a seguinte frase: "A soma entre <X> e <Y> é igual <total>".
"""
num1 = float(input("Informe a primeiro nota: "))
num2 = float(input("Informe a segunda nota: "))
num3 = float(input("Informe a terceira nota: "))
num4 = float(input("Informe a quarta nota: "))

media =  (num1+num2+num3+num4)/4;
print("média = %.2f" %(media))