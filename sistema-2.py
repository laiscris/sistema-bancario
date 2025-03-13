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

limite_saques = 3
saques = 0
limite_valor_saque = 500
saldo = 0
historico = []

def deposito(saldo, valor_deposito):
    saldo += valor_deposito
    mensagem_deposito = f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!'
    return saldo, mensagem_deposito

def saque(saldo, valor_saque, limite_saques, saques):
    saques = 0
    if saldo <= 0:
        return saldo, saques, 'Você ainda não possui saldo. Realize um depósito!'
    if saques >= limite_saques:
        return saldo, saques, 'Limite de saques excedido!'
    if valor_saque > limite_valor_saque:
        return saldo, saques, 'Valor de saque excedido. Seu limite é de R$ 500,00 por saque!'
    saldo -= valor_saque
    saques += 1
    mensagem_saque = f'Saque de R$ {valor_saque:.2f} realizado com sucesso!'
    return saldo, saques, mensagem_saque

def extrato(historico, saldo):
    print("\n=== EXTRATO BANCÁRIO ===")
    if not historico:
        print("Nenhuma movimentação realizada.")
    else:
        for transacao in historico:
            print(transacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

while True:
    opcao = input('''
Escolha a operação que deseja fazer das opções abaixo:
    [1] Sacar
    [2] Depositar
    [3] Visualizar extrato 
    [4] Sair
''')

    if opcao == '1': # Saque
        valor_saque = int(input('Valor do saque: '))
        saldo, saques, mensagem_saque = saque(saldo, valor_saque, limite_saques, saques)
        print(mensagem_saque)
        if 'sucesso' in mensagem_saque:
            historico.append(mensagem_saque)

    elif opcao == '2': # Depósito
        valor_deposito = int(input('Valor do depósito: '))
        saldo, mensagem_deposito = deposito(saldo, valor_deposito)
        print(mensagem_deposito)
        historico.append(mensagem_deposito)

    elif opcao == '3': # Extrato
        extrato(historico, saldo)

    elif opcao == '4': # Sair
        print('Obrigada por utilizar o nosso sistema!!!')
        break

    else:
        print('Escolha uma opcao de 1 a 4 apenas!')


