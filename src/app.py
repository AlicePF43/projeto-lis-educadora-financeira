import json
import pandas as pd
import streamlit as st

# ============ 1. CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')

# ============ 2. INICIALIZAR MEMÓRIA ============
if "historico" not in st.session_state:
    st.session_state.historico = []

# ============ 3. FUNÇÃO DE DEMONSTRAÇÃO ============
def resposta_demo(pergunta):
    """Respostas automáticas para o modo de demonstração na DIO."""
    pergunta = pergunta.lower()
    if "gastos" in pergunta or "gastei" in pergunta:
        return f"Laura, analisei seus dados! Seus maiores gastos este mês foram com Moradia (R$ 1.200) e Alimentação (R$ 450). Juntos, eles representam a maior parte das suas despesas."
    elif "meta" in pergunta or "reserva" in pergunta:
        return f"Laura, faltam R$ 5.000 para atingir sua meta de R$ 15.000. Se você poupar R$ 500 por mês, chegará lá em 10 meses!"
    elif "investir" in pergunta or "produto" in pergunta:
        return "Para sua reserva de emergência, as melhores opções no nosso catálogo são o Tesouro Selic ou o CDB de Liquidez Diária, pois oferecem segurança e resgate rápido."
    else:
        return "Olá! Sou a Lis. Como estou em modo de demonstração, posso te ajudar a analisar seus gastos, falar sobre sua meta de reserva ou explicar produtos financeiros. O que deseja saber?"

# ============ 4. INTERFACE (VISUAL) ============
st.set_page_config(page_title="Lis - Modo Demo", layout="centered")
st.title("👩‍🏫 Lis, sua Educadora Financeira")
st.info("🚀 MODO DE DEMONSTRAÇÃO ATIVO: A Lis está respondendo com base na lógica local do projeto.")
st.markdown(f"Olá, **{perfil['nome']}**! Como posso te ajudar hoje?")
st.markdown("---")

for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    with st.spinner("Lis processando dados..."):
        resposta = resposta_demo(pergunta)
        resposta = resposta_demo(pergunta)
        st.session_state.historico.append({"role": "user", "content": pergunta})
        st.session_state.historico.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.markdown(resposta)

if st.sidebar.button("Limpar Conversa"):
    st.session_state.historico = []
    st.rerun()
