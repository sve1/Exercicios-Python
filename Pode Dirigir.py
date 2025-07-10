#Pedir a idade da pessoa. 
#Perguntar se ela possui CNH (responder sim ou não). 
#Verificar se tem 18 anos ou mais e se respondeu “sim” para CNH. 
#Mostrar se pode ou não dirigir. 

idade = int(input("Qual a sua idade?"))
cnh = input("Você possui CNH ?")
resposta_cnh = "SIM"
resposta_cnh2 = "NÃO"

if (idade >=18) and cnh == resposta_cnh:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir")
    