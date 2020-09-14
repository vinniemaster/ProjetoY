import pymysql.cursors


connection = pymysql.connect(host = 'localhost',
                            user='root',
                            passwd='Amil@2020',
                            db='estoquev2',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


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

    with connection.cursor() as cursor:
        sql = "INSERT INTO 'PRODUTO'('DESCRICAO','TIPO','FORNECEDOR','ESTOQ_MIN','ESTOQ_INI','ESTOQ_ATUAL') VALUES (%S,%S,%S,%S,%S,%S)"
        cursor.execute(sql,(prod.descricao,prod.tipo,prod.fornecedor,prod.estoq_min,prod.estoq_ini,prod.estoq_atual))
        connection.commit()
        

def consulta_prod():

    with connection.cursor() as cursor:
        sql = "SELECT * FROM PRODUTO WHERE 'ID_PRODUTO' >=%S"
        cursor.execute(sql,('0',))
        for item in cursor.fetchall():
            print(item)
        connection.close()