import streamlit as st
import pandas as pd

st.set_page_config(page_title="LLCOMPANY - Gestora", layout="wide")

st.title("🏦 LLCOMPANY | Gestão de Ativos")
st.markdown("---")

st.sidebar.header("Menu de Navegação")
opcao = st.sidebar.selectbox("Escolha uma visualização", ["Visão Geral", "Carteira de Clientes"])

if opcao == "Visão Geral":
    st.subheader("Resumo do Fundo")
    col1, col2 = st.columns(2)
    col1.metric("Total sob Gestão", "R$ 185.000,00", "+5.2%")
    col2.metric("Clientes Ativos", "3", "Novo cliente hoje")

elif opcao == "Carteira de Clientes":
    st.subheader("Detalhamento por Cliente")
    # Simulação de dados (depois conectaremos ao banco real do Databricks)
    dados = {
        'Cliente': ['Ana Silva', 'Bruno Costa', 'Carla Dias'],
        'Perfil': ['Moderado', 'Arrojado', 'Conservador'],
        'Patrimônio': [70000, 100000, 15000]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df, use_container_width=True)
