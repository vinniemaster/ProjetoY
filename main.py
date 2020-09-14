import estoque

while True:
    try:
        print('***Controle de Estoque***')
        opt = int(input('1 - Menu Cadastro\n 2 - Sair\nEscolha: '))

        if (opt == 1):
            estoque.cadastro_prod()
            print('Produto cadastrado com sucesso !!')
        
        elif (opt == 2):
            estoque.consulta_prod()
            clear()
            break
