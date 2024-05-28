#Projeto de banco simples - Dar ao usuário as opções de extrato, saque, depósito, e sair

import time

saldo = 0
extrato = ""
saques = 0
limite_saques = 3
limite_saldo = 500


def depositar():
    global saldo
    global extrato
    valor_deposito = float(input("Informe o valor a ser depositado: \n"))
    
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"Depósito de R${valor_deposito:.2f} feito")
        extrato += f'Depósito de R${valor_deposito:.2f} feito. \n'
    
    else:
        print("Erro. O valor informado é inválido.")

def sacar():
    global saldo
    global extrato
    global saques
    
    valor_saque = float(input("Informe o valor a ser sacado: \n"))
    
    break_saque = saques >= limite_saques
    
    
    if valor_saque > saldo:
        print("Sinto muito, você não tem saldo suficiente.")
    
    elif valor_saque > limite_saldo:
        print("Sinto muito. Você excedeu seu valor limite de saque diário.")
    
    elif break_saque:
        print("Sinto muito. Você já realizou a quantidade de saques diários.")
    
    elif valor_saque > 0:
        saldo -= valor_saque
        print(f"Saque de R${valor_saque:.2f} feito \n O seu valor atual é de R${saldo}.")
        extrato += f'Saque de R${valor_saque:.2f} feito.'
        
        saques += 1
        print(f"Você já fez {saques} saques hoje.")
    
    else:
        print("Erro. O valor informado é inválido.")
    
def ver_extrato():
    print(f"""
Seu valor atual é de R${saldo:.2f}
O seu histórico atual consta com as seguintes movimentações:
{extrato}
""")
    

while True:
    print("""
    ------------------ Banco Virtual em Python! ------------------------
        Bom dia, o que você deseja realizar hoje?
    """)
    
    operacao = int(input("\n - Digite 1 para Depositar\n - Digite 2 para Sacar \n - Digite 3 para visualizar seu Extrato \n - Digite 4 para sair \n"))
    
    if operacao == 1:
        depositar()
        time.sleep(2)
    elif operacao == 2:
        sacar()
        time.sleep(2)
    elif operacao == 3:
        ver_extrato()
        time.sleep(4)
    elif operacao == 4:
        break
    else:
        print("Erro. O número informado é inválido.")