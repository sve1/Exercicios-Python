#Pedir a nota (entre 0 e 10). 
#Se for 7 ou mais, o aluno está aprovado. 
#Se estiver entre 5 e 6.9, está em recuperação. 
#Se for menor que 5, está reprovado. 
#Mostrar o resultado. 

nota = float(input("Qual a sua nota?"))

if(nota >= 7): 
    print("Você está aprovado!")
elif(nota < 5):
    print("Você está reprovado")
else:
    print("Você está de recuperação!")

    