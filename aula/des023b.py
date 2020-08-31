#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Informe um numero: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Milhar: {}'.format(n[0]))
print('Centena: {}'.format(n[1]))
print('Dezena: {}'.format(n[2]))
print('Unidade: {}'.format(n[3]))



