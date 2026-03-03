import streamlit as st

# Título da Aplicação
st.title('Hello World!')

# Escreve uma mensagem na tela
st.write('Esta é uma página de exemplo criada com o Streamlit.')

# Adicionando um pouco mais de interatividade
st.header('Componentes do Streamlit')

# Caixa de seleção
if st.checkbox('Mostrar mensagem secreta'):
    st.write('Você descobriu a mensagem secreta! 🎉')

# Botão
if st.button('Clique em mim'):
    st.balloons()
    st.success('Você clicou no botão!')

