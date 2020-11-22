#Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
##– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = (float(input('Preço das compras: R$ ')))
print('''FORMAS DE PAGAMENTO
[1] a vista no dinheiro/cheque
[2] a vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção: '))
if opção==1:
    total = preço-(preço *10 /100)
elif opção ==2:
    total = preço - (preço * 5 /100)
elif opção == 3:
    total = preço
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção ==  4:
    total = preço +(preço * 20/100)
    totalpc = int(input('Quantas parcelas: '))
    parcela = total/totalpc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(totalpc, parcela))
else:
    total = preço
    print('\033[32m OPÇÃO INVÁLIDA\033[m de pagamento.Tente novamente!')
print('Sua compra de R${:.2f} vai custar R$ {} no final.'.format(preço, total))

