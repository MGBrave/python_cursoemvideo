#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
#métodos
a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('Está em maiúscula? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('É um número ou um nome? ',a.isalnum())
print('Está capitalizada? ', a.istitle())#nem maiúsculas nem minúsculas

