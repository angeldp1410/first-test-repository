#Escribir un programa que almacene la cadena de caracteres contraseña y también usuario
#cada una en sus respectivas variables, para que después,
#pregunte al usuario por la contraseña y el usuario hasta que introduzca
#la contraseña correcta y usuario correcta.

pasword = 'papugit'

text_input = input('Por favor ingrese su contraseña')



while text_input != pasword:
    text_input = input('Por favor ingrese su contraseña')
    
print('Contraseña correcta :)')