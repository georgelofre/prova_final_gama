from pymongo import MongoClient

def obter_colecao_mongodb(uri):
    cliente = MongoClient(f'{uri}')
    nome_do_banco = cliente[f'{nomebanco}']
    colecao = nome_do_banco['teste']
    base_inicial = {"sku": 'abc', "estoque": 10}
    colecao.insert_one(base_inicial)

def ajustar_estoque(sku, estoque, colecao):
    colecao.update_one({"sku": sku}, {"$set": {"estoque": estoque}})


uri = input('Digite a uri de conexão: ').strip()
colecao = input('Digite o nome da coleção desejada: ')

obter_colecao_mongodb()

sku = input('Digite o sku: ')
estoque = int(input('Novo valor do estoque: '))
ajustar_estoque(sku, estoque, colecao)



