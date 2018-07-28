"""
F Faça um algoritmo em que o usuário informe uma medida em metros. Em seguida, converta
 essa medida para centímetros e envie para a saída padrão:
"""
num1 = float(input("Informe a metragem: "))

centimetro = num1*100
metro = "metros"


print("%.2f %s = %.2f centimentros" %(num1, metro, centimetro))