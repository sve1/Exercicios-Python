#Pedir a idade da criança. 
#Verificar se a idade é menor ou igual a 12. 
#Mostrar mensagem informando se o ingresso é gratuito ou não. 

idade = int(input("Qual a sua idade ?"))

if(idade <= 12):
    print("Ingresso gratuito")
else:
    print("Pagar R$10,00")