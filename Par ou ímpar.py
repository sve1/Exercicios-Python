#Pedir um número ao usuário. 
#Verificar se o número dividido por 2 tem resto 0. 
#Se tiver, é par; senão, é ímpar. 
#Mostrar o resultado. 

num = int(input("Digite um número:"))
num2 = 2

if(num % num2 == 0):
    print("Número Par")
else:
    print("Número Ímpar")