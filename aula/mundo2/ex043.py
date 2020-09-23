#Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input('Qual é o seu peso:(kg) '))
altura = float(input('Qual é o sua altura:(m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO do peso normal')
elif imc>= 18.5 and imc < 25: # pode fazer desta forma tambem elif 18.5<=18.5 imc < 25:
    print('PARABÉNS, voce esta na faixa de peso NORMAL')
elif 25 <= imc < 30:
    print('VOCE  esta EM SOBREPESO')
elif 30 <= imc < 40:
    print('VOCE  esta EM OBESIDADE')
elif imc >= 40:
    print('VOCE  esta OBESIDADE MÓRBIDA, cuidado!')


