#Pedir a idade da pessoa. 
#Verificar se está entre 16 e 65 anos (inclusive). 
#Mostrar se a entrada é permitida ou negada. 

idade = int(input("Qual a sua idade?"))
if(idade >= 16) and (idade<=65):
    print("Entrada Permitida!")
else:
    print("Não pode entrar!")