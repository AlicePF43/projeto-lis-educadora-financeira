import json
import pandas as pd
import streamlit as st

# ============ 1. CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')

# ============ 2. INICIALIZAR MEMÓRIA ============
if "historico" not in st.session_state:
    st.session_state.historico = []

# ============ 3. FUNÇÃO DE DEMONSTRAÇÃO MELHORADA ============
def resposta_demo(pergunta):
    p = pergunta.lower()
    if "gastos" in p or "gastei" in p or "dinheiro" in p:
        return f"Laura, analisando seus dados, notei que sua maior despesa é Moradia (R$ 1.200). Você tem um saldo positivo este mês, o que é ótimo para sua reserva!"
    elif "meta" in p or "reserva" in p or "quanto falta" in p:
        return f"Faltam exatamente R$ 5.000 para sua meta de R$ 15.000. Se mantiver o ritmo de R$ 500/mês, em 10 meses você atinge o objetivo!"
    elif "investir" in p or "produto" in p or "onde guardar" in p:
        return "Para sua segurança, recomendo o Tesouro Selic ou CDB Liquidez Diária. Eles são ideais para sua Reserva de Emergência."
    elif "oi" in p or "olá" in p or "quem é você" in p:
        return f"Olá, Laura! Sou a Lis, sua educadora financeira. Posso te ajudar a analisar seus gastos, simular sua meta ou explicar investimentos. O que vamos ver hoje?"
    else:
        # Resposta para perguntas fora de contexto
        return "Laura, como sua educadora financeira, meu foco é te ajudar com seu dinheiro e metas. Que tal falarmos sobre seus gastos ou sua reserva de emergência?"

# ============ 4. INTERFACE (VISUAL) ============
st.set_page_config(page_title="Lis - Educadora Financeira", layout="centered")
st.title("👩‍🏫 Lis, sua Educadora Financeira")
st.markdown(f"Olá, **{perfil['nome']}**! Como posso te ajudar hoje?")
st.markdown("---")

for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    with st.spinner("Lis processando..."):
        resposta = resposta_demo(pergunta)
        st.session_state.historico.append({"role": "user", "content": pergunta})
        st.session_state.historico.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.markdown(resposta)

if st.sidebar.button("Limpar Conversa"):
    st.session_state.historico = []
    st.rerun()
