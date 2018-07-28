# coding: UTF-8

"""
 Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas,
  minutos e segundos. Em seguida, converta tudo para segundos:
"""
#todo
dia = int(input("Dias: "))
hora = int(input("HS: "))
minuto = int(input("Min: "))
segundo = int(input("seg: "))

dias_segundos = dia*24*60*60
hora_segundo = (hora*60)*60
minuto_segundo = minuto*60
segundos = dias_segundos+hora_segundo+minuto_segundo+segundo

print("A quantidade total de segundos é de %d" %segundos)