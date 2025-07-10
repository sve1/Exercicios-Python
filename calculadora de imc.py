#Pedir o peso (em kg) e altura (em metros). 
#Calcular o IMC usando a fórmula: peso dividido pela altura ao quadrado. 
#Comparar o valor do IMC com as faixas: 
#Menor que 18.5: Abaixo do peso 
#Entre 18.5 e 24.9: Peso normal 
#Entre 25 e 29.9: Sobrepeso 
#30 ou mais: Obesidade 
#Mostrar a classificação. 

peso = float(input("Qual seu peso?"))
altura = float(input("Qual a sua altura?"))
calculo_imc = (peso / altura**2)
print(calculo_imc)

if(calculo_imc < 18.5):
    print("Abaixo do Peso")
elif(calculo_imc >= 18.5 and calculo_imc<=24.9):
    print("Peso Normal")
elif(calculo_imc >=25 and calculo_imc<=29.9):
    print("Sobrepeso")
elif(calculo_imc>=30):
    print("Obesidade")