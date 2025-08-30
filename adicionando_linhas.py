from datetime import datetime
import streamlit as st
import pandas as pd

caminho_datasets = 'datasets'

df_compras = pd.read_csv(f'{caminho_datasets}/compras.csv', decimal=',', sep=';') 
df_lojas = pd.read_csv(f'{caminho_datasets}/lojas.csv', decimal=',', sep=';')
df_produtos = pd.read_csv(f'{caminho_datasets}/produtos.csv', decimal=',', sep=';')

df_lojas['cidade/estado'] = df_lojas['cidade'] + '/' + df_lojas['estado'] # criando nova coluna
lista_lojas = df_lojas['cidade/estado'].to_list() # convertendo para lista
st.selectbox('Seleciona a Loja', lista_lojas)