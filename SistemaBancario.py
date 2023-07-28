import datetime
from time import sleep
import textwrap

#CORES
VERMELHA = "\033[31m" 
BRANCA = "\033[0;37m" 
VERDE = "\033[32m"
AMARELA = "\033[33m"

def menu():
    menu = f"""{BRANCA}
[D] - Depositar
[S] - Sacar
[E] - Extrato
[NC] - Nova conta
[LC] - Listar contas
[NU] - Novo usuário
[Q] - Sair
>>>"""
    return input(textwrap.dedent(menu)).upper()


def depositar(saldo, valor, extrato):
    if(valor>0):
        saldo += valor
        data = (f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute} ")
#o comando acima pega o horário em que a operação foi feita
        extrato += str(f"{data}Depositou {valor:.2f} reais\n")
        sleep(0.5)
        print(f"\n{VERDE}Valor depositado com sucesso!")
    else:
        print(f"{VERMELHA}ERRO! Valor inválido!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, num_saques, valor_diario_sacado, LIMITE_SAQUE):
    if(num_saques<3 and (valor_diario_sacado+valor)<LIMITE_SAQUE and valor<saldo):
        saldo -= valor
        valor_diario_sacado += valor
        num_saques += 1
        data = (f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute} ")
        extrato += str(f"{data}Sacou {valor:.2f} reais\n")
        sleep(0.5)
        print(f"\n{VERDE}Saque realizado! Retire o dinheiro na boca do caixa.")
    else:
        sleep(0.5)
        print(SAQUE_ERRO_MSG)
        sleep(1.5)
    return saldo, extrato, num_saques, valor_diario_sacado

def mostrar_extrato(saldo, /, *, extrato, num_saques, valor_diario_sacado, LIMITE_SAQUE):
    sleep(0.5)
    print(extrato)
    sleep(1)
    dados_extrato = (f"""
Você já realizou {num_saques} dos seus 3 Saques Diários
Sacou {valor_diario_sacado} R$ de seu limite diário de {LIMITE_SAQUE} R$
Seu saldo atual é de: {saldo} R$""")
    print(dados_extrato)
    sleep(2.5)

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{VERMELHA}ERRO! Já existe um usuário com esse CPF!{BRANCA}")
        return

    nome = input("Informe seu o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(f"\n{VERDE}Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{VERDE}Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(f"\n{VERMELHA}Usuário não encontrado, fluxo de criação de conta encerrado!{BRANCA}")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
#    LIMITE_SAQUES = 3 #Vezes por dia
    LIMITE_SAQUE = 500 #Quantidade
    AGENCIA = "0001"

    saldo = 0
    num_saques = 0
    valor_diario_sacado = 0
    extrato = "\n"
    usuarios = []
    contas = []
    while True:
        opcao = menu()

        if(opcao=="D"):
            valor = float(input("Digite um valor para depositar: "))
            saldo, extrato = depositar(saldo,valor,extrato)
            

        elif (opcao=="S"):
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, num_saques, valor_diario_sacado = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                num_saques=num_saques,
                valor_diario_sacado=valor_diario_sacado,
                LIMITE_SAQUE=LIMITE_SAQUE,
            )

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

            
        elif (opcao=="E"):
            mostrar_extrato(
            saldo, extrato=extrato, 
            num_saques=num_saques, 
            valor_diario_sacado=valor_diario_sacado,
            LIMITE_SAQUE=LIMITE_SAQUE)
        
        elif (opcao=="Q"):
            sleep(0.5)
            print(f"{VERDE}Até mais, volte sempre que precisar!\n{BRANCA}")
            sleep(0.5)
            break

        else:
            print(f"{VERMELHA}Operação inválida, por favor selecione a operação desejada.")



SAQUE_ERRO_MSG = (f"""{VERMELHA}
ERRO NO SAQUE! Três possíveis erros podem ter acontecido.
1 - O valor ultrapassa o seu limite diário de saque.
2 - Você já fez quantidade máxima de saques diários.
3 - Não há saldo suficiente na conta para fazer esse saque.
          
{AMARELA}Para ter mais informações acesse o seu extrato\n.""")

main()

