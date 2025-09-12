import pandas as pd
import streamlit as st
from datetime import date, time, timedelta

PERCENTUAL_COMISSAO = 0.05
COLUNAS_ANALISE = ['loja', 'vendedor', 'produto', 'cliente_genero', 'forma_pagamento']
COLUNAS_NUMERICAS = ['preco', 'comissao']
FUNCOES_AGREGACAO = {'soma': 'sum', 'contagem': 'count'}

caminho_datasets = 'datasets'


df_compras = pd.read_csv(f'{caminho_datasets}/compras.csv', decimal=',', sep=';', index_col=0, parse_dates=True)
df_lojas = pd.read_csv(f'{caminho_datasets}/lojas.csv', decimal=',', sep=';', index_col=0)
df_produtos = pd.read_csv(f'{caminho_datasets}/produtos.csv', decimal=',', sep=';', index_col=0)

df_produtos = df_produtos.rename(columns={'nome': 'produto'})
df_produtos.reset_index()

df_produtos = pd.merge(
    left=df_produtos,
    right=df_compras[['produto', 'preco']],
    on='produto',
    how='left'
)

df_compras = df_compras.set_index('data')
df_compras['comissao'] = df_compras['preco'] * PERCENTUAL_COMISSAO

