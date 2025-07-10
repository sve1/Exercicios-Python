import hashlib 
senha = input("Digite a senha:")
senha_hash = hashlib.sha256(senha.encode()).hexdigest()
print("O hash da sua senha é:", senha_hash)