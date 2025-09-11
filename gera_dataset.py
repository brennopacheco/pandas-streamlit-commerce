# Gerando mais dados de treinamento a partir dos dados originais usando técnicas de aumento de dados (looping)
import random # módulo nativo
from datetime import datetime, timedelta # módulo nativo
from pathlib import Path # módulo nativo
import pandas as pd 
import names

pasta_datasets = Path(__file__).parent / 'datasets' # pasta onde estão os datasets

pasta_datasets.mkdir(parents=True, exist_ok=True) # criando a pasta

LOJAS = [
    {"estado": "SP", "cidade": "São Paulo", 
    "vendedores":["Ana Oliveira", "Lucas Pereira"]},
    {"estado": "MG", "cidade": "Belo Horizonte", 
    "vendedores":["Carlos Silva", "Fernanda Costa"]},
    {"estado": "RJ", "cidade": "Rio de Janeiro", 
    "vendedores":["Juliana Almeida", "Pedro Souza"]},
    {"estado": "RS", "cidade": "Porto Alegre", 
    "vendedores":["Mariana Gomes", "Roberto Ferreira"]},
    {"estado": "SC", "cidade": "Florianópolis", 
    "vendedores":["Gabriela Santos", "Tiago Lima"]},
    {"estado": "MA", "cidade": "São Luís", 
    "vendedores":["Brenno Pacheco", "Emanuelle Victoria"]},
    {"estado": "PE", "cidade": "Recife", 
    "vendedores":["Ricardo Mendes", "Patrícia Carvalho"]},
    {"estado": "CE", "cidade": "Fortaleza", 
    "vendedores":["André Lima", "Beatriz Rocha"]},
    {"estado": "RN", "cidade": "Natal", 
    "vendedores":["João Matos", "Larissa Ferreira"]}
]

PRODUTOS = [
    {"nome": "Smartphone Samsung Galaxy", "id": 0, "preco": 2500},
    {"nome": "Notebook Dell Inspiron", "id": 1, "preco": 4500},
    {"nome": "Tablet Apple Ipad", "id": 2, "preco": 3000},
    {"nome": "Smartwatch Garmin", "id": 3, "preco": 1200},
    {"nome": "Fone de Ouvido Sony", "id": 4, "preco": 600},
    {"nome": "iPhone 13", "id": 5, "preco": 3600},
    {"nome": "Monitor LG Ultrawide", "id": 6, "preco": 1800},
    {"nome": "Teclado Mecânico HyperX", "id": 7, "preco": 450},
    {"nome": "Mouse Gamer Logitech", "id": 8, "preco": 350},
    {"nome": "Câmera Canon EOS", "id": 9, "preco": 5200},
]

FORMA_PAGTO = ["cartão de crédito", "boleto", "pix", "dinheiro", "cartão de dédito"]

GENERO_CLIENTES = ["male", "female"]

# Gerar a patir dos dados acima um dataset com 2000 compras
compras = []
# Looping para gerar 4000 compras
for _ in range(4000):
    loja = random.choice(LOJAS) # escolhe uma loja aleatória
    vendedor = random.choice(loja["vendedores"]) # escolhe um vendedor aleatório da loja
    produto = random.choice(PRODUTOS) # escolhe um produto aleatório
    hora_compra = datetime.now() - timedelta(
        days=random.randint(1, 365), # variação de até 365 dias
        hours=random.randint(-5, 5), # variação de até 5 horas
        minutes=random.randint(-30, 30) # variação de até 30 minutos
    )
    genero_cliente = random.choice(GENERO_CLIENTES) # escolhe um gênero aleatório
    nome_cliente = names.get_full_name(gender=genero_cliente) # gera um nome aleatório
    forma_pgto = random.choice(FORMA_PAGTO) # escolhe uma forma de pagamento aleatória

    compras.append({
        'data': hora_compra,
        'id_compra': 0, # preencher depois
        'loja': loja["cidade"],
        'vendedor': vendedor,
        'produto': produto["nome"],
        'cliente_nome': nome_cliente,
        'cliente_genero': genero_cliente.replace('female', 'feminino').replace('male', 'masculino'),
        'forma_pagamento': forma_pgto
    })


df_compras = pd.DataFrame(compras).set_index('data').sort_index() # transforma em dataframe, seta a data como índice e ordena pela data
df_compras["id_compra"] = [i for i in range(len(df_compras))] # preenche o id_compra com números sequenciais

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)

# Exportar os datasets para arquivos CSV
df_compras.to_csv(pasta_datasets / 'compras.csv', decimal=',', sep=';', date_format='%Y-%m-%d %H:%M:%S')  # <-- garante padrão sem microssegundos
df_lojas.to_csv(pasta_datasets / 'lojas.csv', decimal=',', sep=';')
df_produtos.to_csv(pasta_datasets / 'produtos.csv', decimal=',', sep=';')

# Exportar os datasets para arquivos Excel
df_compras.to_excel(pasta_datasets / 'compras.xlsx')
df_lojas.to_excel(pasta_datasets / 'lojas.xlsx')
df_produtos.to_excel(pasta_datasets / 'produtos.xlsx')