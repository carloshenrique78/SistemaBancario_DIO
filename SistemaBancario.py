import datetime
from time import sleep

#Adicionei algumas coisas a mais para o programa ficar mais interessante

VERMELHA = "\033[31m" 
BRANCA = "\033[0;37m" 
VERDE = "\033[32m"
AMARELA = "\033[33m"


saldo = 0
num_saques = 0
valor_diario_sacado = 0
extrato = "\n"
LIMITE_SAQUE = 500

menu = f"""{BRANCA}
[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair
>>>"""

SAQUE_ERRO_MSG = (f"""{VERMELHA}
ERRO NO SAQUE! Três possíveis erros podem ter acontecido.
1 - O valor ultrapassa o seu limite diário de saque.
2 - Você já fez quantidade máxima de saques diários.
3 - Não há saldo suficiente na conta para fazer esse saque.
          
{AMARELA}Para ter mais informações acesse o seu extrato\n.""")



def checarconta():
    dados_extrato = (f"""
Você já realizou {num_saques} dos seus 3 Saques Diários
Sacou {valor_diario_sacado} R$ de seu limite diário de {LIMITE_SAQUE}
Seu saldo atual é de: {saldo} R$\n""")
    print(dados_extrato)

"""
a função acima foi criada pois existia um bug que 
os valores apareciam zerados como no início do programa
"""

while True:
    opcao = input(menu).upper()

    if(opcao=="D"):
        deposito = int(input("Digite um valor para depositar: "))
        if(deposito>0):
            saldo += deposito
            data = (f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute} ")
            #o comando acima pega o horário em que a operação foi feita
            extrato += str(f"{data}Depositou {deposito} reais\n")
            print(f"{VERDE}Valor depositado com sucesso!")
        else:
            print(f"{VERMELHA}ERRO! Valor inválido!")

    elif (opcao=="S"):
        saque = int(input("\nDigite o valor que deseja sacar: "))
        if(num_saques<3 and (valor_diario_sacado+saque)<LIMITE_SAQUE and saque<saldo):
            saldo -= saque
            valor_diario_sacado += saque
            num_saques += 1
            data = (f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute} ")
            extrato += str(f"{data}Sacou {saque} reais\n")
            print(f"\n{VERDE}Saque realizado! Retire o dinheiro na boca do caixa.")
        else:
            sleep(0.8)
            print(SAQUE_ERRO_MSG)
            sleep(1.5)
        
    elif (opcao=="E"):
        sleep(1)
        print(extrato)
        sleep(1.5)
        checarconta()
        sleep(2.5)
    
    elif (opcao=="Q"):
        sleep(0.8)
        print(f"\n{VERDE}Muito obrigado, volte sempre!\n{BRANCA}")
        break

    else:
        print(f"{VERMELHA}Operação inválida, por favor selecione a operação desejada.")