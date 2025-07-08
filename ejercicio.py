#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario la contraseña y al alcanzar los 3 intentos este se bloquee.

pasword = 'papugit'
sentinel = 1

text_input = input('Por favor ingrese su contraseña: ')

while text_input != pasword:
    sentinel += 1
    
    if sentinel > 3:
        print('Contraseña incorrecta :(')
        break
    
    text_input = input('Por favor ingrese su contraseña: ')
    
if sentinel <= 3:
        print('Contraseña correcta :)')
    
    
       
    