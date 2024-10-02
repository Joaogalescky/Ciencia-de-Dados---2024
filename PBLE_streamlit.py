import streamlit as st
import pandas as pd

# Carregar dados do arquivo csv
database_path = 'databases/pble.csv' # Caminho do arquivo
df = pd.read_csv(database_path, encoding='latin-1') # Carregar a base

# Carregar dados do arquivo xlsx
# xlsx_path = 'databases/RELATORIO_DTB_BRASIL_MUNICIPIO.xlsx'
# df_xlsx = pd.read_excel(xlsx_path)

st.title('Programa Banda Larga nas Escolas')

st.dataframe(df)