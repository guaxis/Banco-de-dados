import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(page_title="LLCOMPANY - Gestora", layout="wide")

# 2. Título Principal
st.title("🏦 LLCOMPANY | Gestão de Ativos")
st.markdown("---")

# 3. Menu Lateral
st.sidebar.header("Menu de Navegação")
opcao = st.sidebar.selectbox(
    "Escolha uma visualização", 
    ["Visão Geral", "Carteira de Clientes", "Performance de Ativos"]
)

# 4. Lógica das Abas
if opcao == "Visão Geral":
    st.subheader("📊 Resumo do Fundo")
    col1, col2, col3 = st.columns(3)
    
    # Métricas Simuladas
    col1.metric("Total sob Gestão", "R$ 185.000,00", "+5.2%")
    col2.metric("Clientes Ativos", "3", "Novo cliente hoje")
    col3.metric("Lucro Mensal (Estimado)", "R$ 12.450,00", "+2.1%")

elif opcao == "Carteira de Clientes":
    st.subheader("👥 Detalhamento por Cliente")
    
    # Dados Simulados (Substituem a leitura do Banco de Dados por enquanto)
    dados = {
        'Cliente': ['Ana Silva', 'Bruno Costa', 'Carla Dias'],
        'Perfil': ['Moderado', 'Arrojado', 'Conservador'],
        'Patrimônio (R$)': [70000, 100000, 15000],
        'Status': ['Ativo', 'Ativo', 'Pendente']
    }
    df = pd.DataFrame(dados)
    st.table(df)

elif opcao == "Performance de Ativos":
    st.subheader("📈 Performance da Carteira (BTC/ETH/SOL)")
    st.info("Conexão com API de preços em tempo real será configurada no próximo sprint.")
    
    # Gráfico Simples de Exemplo
    chart_data = pd.DataFrame({
        "Dias": list(range(1, 8)),
        "Retorno (%)": [1.2, 1.5, 1.1, 1.8, 2.3, 2.1, 2.5]
    })
    st.line_chart(chart_data.set_index("Dias"))

# Rodapé
st.markdown("---")
st.caption("© 2026 LLCOMPANY - Sistema Interno de Gestão")
