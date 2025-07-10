#Pedir a idade da pessoa. 
#Verificar se a idade é maior ou igual a 16. 
#Informar se a pessoa pode ou não votar. 

idade = int(input("Qual a sua idade ?"))

if(idade >= 16):
    print("Você pode votar!")
else:
    print("Você ainda não pode votar!")