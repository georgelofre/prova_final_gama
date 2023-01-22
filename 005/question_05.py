from pymongo import MongoClient

def obter_colecao_mongodb(uri, nomebanco):
    cliente = MongoClient(f'{uri}')
    nome_do_banco = cliente[f'{nomebanco}']
    return nome_do_banco

uri = input('Digite a uri de conexão: ').strip()
colecao = input('Digite o nome da coleção desejada: ')

obter_colecao_mongodb()