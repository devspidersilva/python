idade = int(input("informe a sua idade: \n"))

if(idade >=0):
    if(idade>=18 and idade<65):
        print("Você tem %d anos de idade, logo é maior de idade"%idade)
    elif(idade>0 and idade<18 ):
        print("Você tem %d anos de idade, logo é menor de idade" % idade)
    elif(idade >=65):
        print("Você tem %d anos de idade, logo é idoso" % idade)
    elif(idade == 0):
        print("Você tem %d anos de idade, logo é um bebê"%idade)
else:
    print("idade inválidade!!")