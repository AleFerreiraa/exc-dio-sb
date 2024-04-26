menu = '''
******************
[d] DEPÓSITO
[s] SAQUE
[e] EXTRATO
[q] SAIR
******************

SUA OPÇÃO => '''

saldo = 0
depositos = 0
saques = 0
limite_saque = 500
extrato = ""

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Qual valor deseja depositar: R$ "))

        while valor_deposito <= 0:
            print("ERRO! VALOR INVÁLIDO. DEPÓSITO DEVE SER MAIOR DO QUE R$ 0.00 \nTENTE NOVAMENTE")
            valor_deposito = float(input("Qual valor deseja depositar: R$ "))
            if valor_deposito > 0:
                break
        saldo += valor_deposito
        depositos +=1
        extrato += f'Deposito realizade de R$ {valor_deposito}\n'

    elif opcao == 's':

        if saldo == 0:
            print("ERRO! SUA CONTA NÃO TEM SALDO")
            continue
        elif saques == 3:
            print("LIMITE DE SAQUES DIÁRIOS ATINGIDOS, VOLTE AMANHÃ.")
            continue

        while True:
            valor_saque = float(input("QUAL VALOR DESEJA SACAR: R$ "))

            if valor_saque > 500:
                print("ERRO! LIMITE DE SAQUE DIÁRIO É DE R$ 500.00 \nTENTE NOVAMENTE")
            elif valor_saque <= 0:
                print("ERRO! VALOR MENOR DO QUE R$ 0.00 \nTENTE NOVAMENTE.")
            elif valor_saque > saldo:
                print(f"SALDO INDISPONÍVEL, SALDO EM CONTA É R$ {saldo:.2f} \nTENTE NOVAMENTE")
            else:
                saldo -= valor_saque
                saques += 1
                extrato += f'Saque realizado de R$ {valor_saque}\n'
                break

    elif opcao == 'e':
        print('*************EXTRATO*************')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('*********************************')

    elif opcao == 'q':
        break

    else:
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")