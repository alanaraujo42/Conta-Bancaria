from desenvolvimento.cadastro_contacorrente import cadastro_conta_corrente
from telas.tela import Tela
from time import sleep

# Tela incial do programa
while True:
    exibir = Tela()  # Tela Inicial do programa
    resposta = exibir.tela_inicial()
    if resposta == '1':  # Tela para Login
        resposta = exibir.tela_login()
        if isinstance(resposta, str):  # Se não houver cadastro
            resposta = exibir.tela_cadastro_nao_existe()
            if resposta == '1':  # Se quiser realizar cadastro
                resposta = cadastro_conta_corrente()
                if resposta == 'ERRO':  # Caso o cadastro já exista
                    exibir.tela_cadastro_ja_existente()
                else:
                    exibir.tela_apos_cadastro()
            else:  # Se NÃO quiser realizar cadastro
                print('\n' * 30)
        else:  # Se após login tiver cadastro
            conta = resposta
            while True:  # Acessando a conta
                resposta = exibir.tela_opcoes_da_conta(conta)
                if resposta == '1':  # Se quiser sacar o dinheiro
                    exibir.tela_saque_dinheiro(conta)
                elif resposta == '2':  # Se quiser depositar o dinheiro
                    exibir.tela_deposito_dinheiro(conta)
                    pass
                elif resposta == '0':  # Se quiser sair da conta
                    print('\n' * 30)
                    break
    elif resposta == '2':  # Após Tela Incial, quiser realizar cadastro
        resposta = cadastro_conta_corrente()
        if resposta == 'ERRO':  # Caso o cadastro já exista
            exibir.tela_cadastro_ja_existente()
        else:
            exibir.tela_apos_cadastro()
    elif resposta == '0':  # Após Tela Inicial, quiser sair do banco
        print('Finalizando programa...')
        sleep(3)
        print('\n' * 30)
        break
