#Definir uma senha correta no programa. 
#Pedir que o usuário digite uma senha. 
#Comparar a senha digitada com a correta. 
#Mostrar mensagem de acesso permitido ou negado. 

import hashlib
password_hash = "b25b779b70cc88c42d773db27459bfbdd2f6070137fbd6528f2cb4c7a85e441f"

typ= input("Digite sua senha:")

typ_hash = hashlib.sha256(typ.encode()).hexdigest()

if (typ == password_hash):
        print("Acesso Permitido")
else:
    print("Acesso Negado!")