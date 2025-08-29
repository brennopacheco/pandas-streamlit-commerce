import streamlit as st
import pandas as pd

caminho_compras = 'datasets/compras.csv'

df_compras = pd.read_csv(caminho_compras, decimal=',', sep=';')

# aplicacao streamlit (web)

st.dataframe(df_compras)