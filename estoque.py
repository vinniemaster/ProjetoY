class Produto:
    def __init__(self, descricao, tipo, fornecedor,estoq_min, estoq_ini,estoq_atual):
        self.descricao = descricao
        self.tipo = tipo
        self.fornecedor= fornecedor
        self.estoq_min = estoq_min
        self.estoq_ini = estoq_ini
        self.estoq_atual = estoq_atual


    def cadastro_prod():

        descricao = input('Digite a descrição do produto: ')
        tipo = input('Qual o tipo do produto: ')
        fornecedor = input('Qual o fornecedor: ')
        estoq_min = input('Quantidade mínima em estoque: ')
        estoq_ini = input('Qual a quantidade inicial do estoque: ')
        estoq_atual = input('Qual a quantidade atual: ')

        prod = Produto(descricao,tipo,fornecedor,estoq_min,estoq_ini,estoq_atual)
        