#Escribir un programa que almacene la cadena de caracteres contraseña y también usuario
#cada una en sus respectivas variables, para que después,
#pregunte al usuario por el usuario y la contraseña y cuando alcanze los 3 intentos este 
#se bloquee.

user = 'papupro'
password = 'papugit'
sentinel = 1


user_input = input('Ingrese su usuario: ')
password_input = input('Ingrese su contraseña: ')

while password_input != password or user != user_input:
    

    sentinel += 1
    
    if sentinel > 3:
        print('Usuario y contraseña incorrecta :(')
        break
    user_input = input('Ingrese su usuario: ')
    password_input = input('Ingrese su contraseña: ')
    
    
    
if sentinel <= 3:
        print('Usuario y contraseña correcta :)')


    
    
       
    