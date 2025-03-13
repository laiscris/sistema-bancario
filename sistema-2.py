# Criar um sistema bancário com as operações de depósito, saque e extrato
# Todos os depósitos e saques devem ser armazenados em variável e exibidos no extrato
# Limite de 3 saques diários de no máximo R$500,00 (verificar se o cliente possui saldo)
# Exibir os valores de saldo final depois das operações no formato R$xxx.xx

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
    opcao = input('Escolha a operação: 1: Depósito; 2: Saque; 3: Extrato; 4: Encerrar\n')

    if opcao == '1':
        valor_deposito = int(input('Valor do depósito: '))
        saldo, mensagem_deposito = deposito(saldo, valor_deposito)
        print(mensagem_deposito)
        historico.append(mensagem_deposito)

    elif opcao == '2':
        valor_saque = int(input('Valor do saque: '))
        saldo, saques, mensagem_saque = saque(saldo, valor_saque, limite_saques, saques)
        print(mensagem_saque)
        if 'sucesso' in mensagem_saque:
            historico.append(mensagem_saque)
        # TO DO: Não adicionar excessos e erros no histórico / extrato

    elif opcao == '3':
        extrato(historico, saldo)

    elif opcao == '4':
        print('Obrigada por utilizar o nosso sistema!!!')
        break

    else:
        print('Escolha uma opcao de 1 a 4 apenas!')


