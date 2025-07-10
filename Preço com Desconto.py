#Pedir ao usuário o valor de um produto (com decimal). 
#Calcular 10% de desconto sobre o valor. 
#Subtrair esse desconto do valor original. 
#Mostrar o valor final com desconto. 

valor = float(input("Qual o valor do produto ?"))
desconto = (valor * 0.10)

print(valor - desconto)