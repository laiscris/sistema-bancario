'''
Operações: SACAR, DEPOSITAR e VISUALIZAR EXTRATO

Saque: 
    - apenas valores positivos 
    - 3 saques diários com limite de R$500 por saque
    - armazenar saques em uma variável e exibir nas operações de extrato 
    - exibir mensagem em caso de erro

Depósito: 
    - apenas valores positivos
    - devem ser armazenados em uma variável e exibidos nas operações de extrato
    - exibir mensagem em caso de erro

Visualizar extrato:
    - listar todos os saques e extratos
    - exibir saldo atual da conta
    - padrão: R$XXXX.XX

'''

menu = ('''
Escolha a operação que deseja fazer das opções abaixo:
    [1] Sacar
    [2] Depositar
    [3] Visualizar extrato 
    [4] Sair 
> ''')

saldo = 0
limite_valor_saque = 500
extrato = ''
num_saques = 0
LIMITE_NUM_SAQUES = 3

while True:
    escolha = input(menu)
    
    if escolha == '1': # Saque

        valor_saque = float(input('Valor do saque: '))

        excedeu_saldo = valor_saque > saldo
        excedeu_num_saque = num_saques > LIMITE_NUM_SAQUES
        excedeu_valor_saque = valor_saque > limite_valor_saque

        if not excedeu_saldo:
            if saldo > 0:
                if valor_saque > 0:
                    if not excedeu_valor_saque:
                        if not excedeu_num_saque:
                            saldo -= valor_saque
                            num_saques += 1
                            extrato += f'Saque: R${valor_saque:.2f} realizado com sucesso!\n'
                        else:
                            print('&& Limite de número de saques diários (3) excedido! &&')
                    else: 
                        print('&& Limite de valor de saque (R$500) excedido! &&')
                else:
                    print('&& Não é possível realizar saques com valores negativos &&')
            else:
                print('&& Saldo insuficiente! Realize um depósito primeiro. &&')
        else:
            print('&& Saque excedeu o valor do saldo! &&')

    elif escolha == '2': # Depósito
        valor_deposito = float(input('Valor do depósito: '))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito: R${valor_deposito:.2f}\n'
        else:
            print('&& Não é possível realizar depósitos com valores negativos &&')

    elif escolha == '3': # Extrato
        print('----------EXTRATO----------')
        print('Nenhuma operação realizada!' if not extrato else extrato)
        print(f'Saldo final: R${saldo:.2f}')
        print('---------------------------')

    elif escolha == '4': # Sair
        print('Obridado por utilizar o nosso sistema!')
        break

    else:
        print('&& Opção inválida! Escolha uma das opções fornecidas. &&')
