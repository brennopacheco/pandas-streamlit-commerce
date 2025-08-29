import streamlit as st
import pandas as pd

caminho_compras = 'datasets/compras.csv'

df_compras = pd.read_csv(caminho_compras, decimal=',', sep=';')

colunas = list(df_compras.columns) # ['data', 'id_compra', 'loja', 'vendedor', 'produto', 'cliente_nome', 'cliente_genero', 'forma_pagamento']

colunas_selecionadas = st.sidebar.multiselect('Selecione as Colunas que deverão Aparecer', colunas, colunas) # adiciona um widget na barra lateral e retorna uma lista com as colunas selecionadas


col_1, col_2 = st.sidebar.columns(2) # cria duas colunas na barra lateral

coluna_filtrada = col_1.selectbox('Seleciona a Coluna para Filtrar', [c for c in colunas if c not in ['id_compra']]) # seleciona a coluna para o filtro, exceto a coluna id_compra

valor_filtro = col_2.selectbox('Selecione o Valor', list(df_compras[coluna_filtrada].unique())) # seleciona o valor para o filtro, baseado na coluna escolhida


st_filtrar = col_1.button('Filtrar')
st_limpar = col_2.button('Limpar Filtros')

if col_1:
    st.dataframe(df_compras.loc[df_compras[coluna_filtrada] == valor_filtro, colunas_selecionadas])
elif st_limpar:
    st.dataframe(df_compras[colunas_selecionadas])
else:
    st.dataframe(df_compras[colunas_selecionadas])