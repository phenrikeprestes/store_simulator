print('{:=^40}'.format('LOJAS CAPELLANO'))
valor = float(input('Valor a ser pago $  '))

print('''
Insira a opção de pagamento desejada
[1] À VISTA (DINHEIRO/CHEQUE)--10% DESC
[2] À VISTA NO CARTÃO--5% DESC
[3] EM ATÉ 2X NO CARTÃO--PREÇO NORMAL
[4] 3X OU MAIS NO CARTÃO--20% DE JUROS

''')
opcao = int(input('Escolha uma opção  '))

if opcao == 1:
    preco = valor - (valor * 10 / 100)
    print(f'O valor a ser pago é de $ {preco :.2f}')
elif opcao == 2:
    preco = valor - (valor * 5 / 100)
    print(f'O valor a ser pago é de $ {preco :.2f}') 
elif opcao == 3:
    parcela = valor / 2
    print(f'O valor a ser pago é de $ {valor} e será parcelada em 2X de $ {parcela :.2f}, sem juros ')  
elif opcao == 4:
    preco = valor + (valor * 20 / 100)    
    totparcelas = int(input('Qual o número de parcelas? '))
    parcela = preco / totparcelas
    print(f'O valor a ser pago é de {preco :.2f} e será parcelada em {totparcelas}X de {parcela :.2f}')
    print(f'Sua compra de {valor :.2f} vai custar {preco :.2f}')

print('Obrigado e volte sempre!')
    
        


