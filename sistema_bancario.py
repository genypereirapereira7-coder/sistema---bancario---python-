saldo = 0
historico = []
while True:
    resposta = input('O que deseja acessar \
                      \n(deposito/saldo/historico/sacar/sair): ').lower()
    if resposta == 'sacar':
        valo = input('Deseja realzar qual valor: ')
        if valo.isdigit():
            numero = int(valo)
            if numero <= saldo:
                if 10 <= numero <= 1000:
                    saldo -= numero
                    historico.append(f'saque {numero}')
                    print(f'Voce sacou {numero} \nSaque realizado com sucesso \nretire seu dinheiro no caixa.  ')   
                else:
                    print('Digite um numero valido.')
            else:
                print('Saldo insuficiente. ')          
        else:
            print('Digite um valor valido. ')
    elif resposta == 'deposito':
        dep = input('Qual valor deseja depositar: ')
        if dep.isdigit():
            dep = int(dep)
            if dep > 5 and dep < 1000:
                saldo += dep
                historico.append(f'deposito {dep}')
                print(f'Voce depositou {dep:.3f} \nDeposito realizado com sucesso.')
            else:
                print('Seu limite foi Excedido. ')
    elif resposta == 'saldo':
        print(f'Seu saldo atual é {saldo}')
    elif resposta == 'historico':
        if not historico:
            print('Nenhuma operacão realizada.')
        else:
            for item in historico:
                print(item)    
    elif resposta == 'sair':
        sair_1 = input('Deseja sair do banco? (s/n)')
        if sair_1 == 's':
            print('Você saiu do banco. ')
            break
    else:
        print('Digite um opçao valida no campo. ')
             
        
