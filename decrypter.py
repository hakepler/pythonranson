import os
import pyaes

## Abre o arquivo criptografado 

file_name = 'olivia.txt.sedeumal'
file = open(file_name, 'rb')
file_data = file.read()
file.close

## chave de descriptografia

key = b'brutuspegouolivi'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove o arquivo criptografado

os.remove(file_name)

## Cria um novo arquivo descriptografado

new_file = 'olivia.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()

