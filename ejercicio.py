#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

pasword = 'papugit'

text_input = input('Por favor ingrese su contraseña')



while text_input != pasword:
    text_input = input('Por favor ingrese su contraseña')
    
print('Contraseña correcta :)')