#Escribir un programa que almacene la cadena de caracteres contraseña y también usuario
#cada una en sus respectivas variables, para que después,
#pregunte al usuario por la contraseña y el usuario hasta que introduzca
#la contraseña correcta y usuario correcta.

user = 'papupro'
password = 'papugit'


user_input = input('Ingrese su usuario: ')
password_input = input('Ingrese su contraseña: ')

while password_input != password or user != user_input:
    user_input = input('Ingrese su usuario: ')
    password_input = input('Ingrese su contraseña: ')
    
print('Usuario y contraseña correcta')

