#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario la contraseña y al alcanzar los 3 intentos este se bloquee.

pasword = 'papugit'

text_input = input('Por favor ingrese su contraseña')

sentinel = 0



while text_input != pasword:
    text_input = input('Por favor ingrese su contraseña')
    sentinel += 1
    
print('Contraseña correcta :)')