import streamlit as st

st.title("CD/TEC")
st.write("Site criado com o Streamlit")

#filmes = ["Forest Gump", "Exterminador do Futuro", "Inception", "Matrix", "Pulp Fiction", 
#"Battleship", "American Gangster", "Interestelar"]

#filme_predileto = st.selectbox("Escolha um filme:", filmes)

#st.write(f"Seu filme predileto é: {filme_predileto}")
#--------------------------------------------------------------------
generos_musicais = ["Rock", "Pop", "Metal", "Reggae", "Jazz", "Eletronica", "Hip Hop"]

#genero_musical = st.selectbox("Escolha um gênero musical:", generos_musicais)

bandas = {
    "Rock": ["Led Zeppelin", "Pink Floyd", "AC/DC", "Queen", "The Beatles"],
    "Pop": ["The Beatles", "", "Michael Jackson", "Elton John", "Queen"],
    "Metal": ["Metallica", "Iron Maiden", "Black Sabbath", "Ozzy Osborne", "Guns N' Roses"],
    "Reggae": ["Bob Marley", "Peter Tosh", "Jimmy Cliff", "Desmond Deck", "Jacob Muller"],
    "Jazz": ["Frank Sinatra", "John Coltrane", "Louis Armstrong", "Billie Holiday", "Ray Charles"],
    "Eletronica": ["Skrillex", "Marshmallow", "Avicii", "Afrojack", "Apache"],
    "Hip Hop": ["Jay-Z", "Eminem", "The Weekend", "Lil Nas X", "Post Malone", "Tupac Shakur", "50 Cent"]
}

genero_musical = st.selectbox("Gênero musical:", bandas.keys())

bandas_predileta = st.selectbox("Escolha sua banda predileta:", bandas[genero_musical])

st.write(f"A melhor banda de {genero_musical} é {bandas_predileta}")

