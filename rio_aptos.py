import streamlit as st
import pandas as pd

st.title('Apartamento na cidade do Rio de Janeiro')

rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')

#st.data_editor(rioAptos)

bairro = st.multiselect("Escolha um bairro:", rioAptos["bairro"].unique())

#st.write(f"Bairro escolhido: {bairro}")

if bairro:
    rioAptosBairro = rioAptos[rioAptos['bairro'].isin(bairro)]
    # isin - gera os números pares compreendidos entre 1 e 10

    menor_preco = rioAptosBairro['preco'].min()
    st.write(f"Menor preço: R$ {menor_preco}")

    maior_preco = rioAptosBairro['preco'].max()
    st.write(f"Maior preço: R$ {maior_preco}")

    valor = st.slider("Faixa de $:", menor_preco, maior_preco, (menor_preco, maior_preco))
    st.write(valor)

    rioAptosBairro = rioAptosBairro[(rioAptosBairro['preco'] >= valor[0]) & (rioAptosBairro['preco'] <= valor[1])]
    st.write(rioAptosBairro)