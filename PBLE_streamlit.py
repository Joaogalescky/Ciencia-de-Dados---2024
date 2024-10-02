import streamlit as st
import pandas as pd

# Carregar dados do arquivo csv
database_path = 'databases/pble.csv' # Caminho do arquivo
df = pd.read_csv(database_path, encoding='latin-1') # Carregar a base

# Carregar dados do arquivo xlsx
xlsx_path = 'databases/RELATORIO_DTB_BRASIL_MUNICIPIO.xlsx'
df_xlsx = pd.read_excel(xlsx_path)

st.write("Aluno: João Vitor Campõe Galescky")
st.write("Curso: 2° Tecnólogo em Análise e Desenvolvimento de Sistemas")

st.title("Programa Banda Larga nas Escolas")
st.write("O Programa Banda Larga na Escola (PBLE) foi lançado em 4 de abril de 2008 pelo Governo Federal, substituindo a obrigatoriedade das operadoras na instalação de Postos de Serviços Telefônicos (PST) pela infraestrutura de rede para suporte a conexão à Internet em alta velocidade para todos os municípios e escolas públicas urbanas.")

dfFilter = df[["sigla_uf", "id_municipio", "rede", "id_escola", "empresa", "tecnologia", "conexao"]]

# Filtros
estado = st.multiselect("Escolha um estado:", dfFilter["sigla_uf"].unique())
if estado: 
    dfUF = dfFilter[dfFilter['sigla_uf'].isin(estado)]
else: 
    dfUF = dfFilter # caso não selecionado, não aplicar o filtro
st.dataframe(dfUF)

empresa = st.multiselect("Escolha uma empresa:", dfFilter["empresa"].unique())
if empresa:
    dfEmpresa = dfUF[dfUF['empresa'].isin(empresa)]
else:
    dfEmpresa = dfUF
st.dataframe(dfEmpresa)

tecnologia = st.multiselect("Escolha uma tecnologia:", dfFilter["tecnologia"].unique())
if tecnologia:
    dfTecnologia = dfEmpresa[dfEmpresa['tecnologia'].isin(tecnologia)]
else:
    dfTecnologia = dfEmpresa
st.dataframe(dfTecnologia)

# menor_conexao = df['conexao'].min()
# st.write(f"Menor conexão: {menor_conexao}")

# maior_conexao = df['conexao'].max()
# st.write(f"Maior conexão: {maior_conexao}")

# conexao = st.slider("Faixa de Internet:", menor_conexao, maior_conexao, (menor_conexao, maior_conexao))
# st.write(conexao)

st.title('Relatório DTB - Brasil - Municípios')
st.dataframe(df_xlsx)