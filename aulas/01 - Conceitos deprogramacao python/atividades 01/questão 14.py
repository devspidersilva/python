"""
Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida, aplique 10% de desconto e imprima
na tela tanto o valor total e também o valor com o desconto aplicado.
"""
#Todo o que deve ser feito
valor = float(input("Valor da compra: "))
desconto = valor*0.10
total = valor - desconto
print("Valor da compra R$:%.2f"%valor)
print("Valor do desconto R$:%.2f"%desconto)
print("Valor total com desconto R$:%.2f"%total)