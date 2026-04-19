import json
import pandas as pd
import streamlit as st
from openai import OpenAI

# ============ 1. CONFIGURAÇÃO (O "Motor") ============
client = OpenAI()
MODELO = "gpt-4.1-mini"

# ============ 2. CARREGAR DADOS (O "Conhecimento") ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ 3. INICIALIZAR MEMÓRIA (O "Histórico") ============
if "historico" not in st.session_state:
    st.session_state.historico = []

# ============ 4. LÓGICA DE SIMULAÇÃO E ANÁLISE (O "Cálculo") ============
meta_valor = 15000.00
reserva_atual = perfil['reserva_emergencia_atual']
valor_que_falta = meta_valor - reserva_atual

# Análise de Gastos (Pandas)
gastos_por_categoria = transacoes[transacoes['tipo'] == 'Despesa'].groupby('categoria')['valor'].sum().sort_values(ascending=False)
resumo_gastos = gastos_por_categoria.to_string()

# ============ 5. BASE DE FAQ (O "Conhecimento do Banco") ============
faq_banco = {
    "FGC": "O Fundo Garantidor de Créditos (FGC) protege seus investimentos em até R$ 250 mil por CPF e por banco, caso a instituição tenha problemas financeiros.",
    "Abertura de Conta": "Para abrir uma conta, você precisa apenas de um documento com foto e ser maior de 18 anos. Tudo é feito pelo nosso app oficial!",
    "Segurança": "Seus dados estão protegidos com criptografia de ponta a ponta e nunca pedimos sua senha por chat ou telefone."
}

# ============ 6. MONTAR O CONTEXTO (A "Memória" da Lis) ============
contexto_dados = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos.
META: Chegar em R$ {meta_valor:,.2f} na Reserva de Emergência.
RESERVA ATUAL: R$ {reserva_atual:,.2f}
FALTAM: R$ {valor_que_falta:,.2f}

RESUMO DE GASTOS: {resumo_gastos}
PRODUTOS DISPONÍVEIS: {json.dumps(produtos, indent=2, ensure_ascii=False)}
FAQ DO BANCO: {json.dumps(faq_banco, indent=2, ensure_ascii=False)}

DADOS DE CÁLCULO (Simulação):
- Se guardar R$ 500/mês: {int(valor_que_falta/500)} meses.
- Se guardar R$ 1.000/mês: {int(valor_que_falta/1000)} meses.
"""

# ============ 7. DEFINIR QUEM É A LIS (A "Personalidade e Segurança") ============
SYSTEM_PROMPT = f"""Você é a Lis, uma assistente educadora financeira amigável e segura.
O seu papel é ajudar a {perfil['nome']} a entender de finanças com base em boas práticas de UX.

REGRAS DE OURO (SEGURANÇA):
1. NUNCA dê conselhos médicos, jurídicos ou recomendações de compra de ações específicas.
2. JAMAIS peça senhas, códigos ou dados sensíveis.
3. Se a pergunta for sobre o banco, use as informações do FAQ fornecido.
4. Mantenha um tom de voz encorajador, didático e profissional.
5. Se não souber algo, admita e sugira que ela fale com um gerente humano.

SUAS TAREFAS:
- Use os dados da {perfil['nome']} para simulações e análise de gastos.
- Explique produtos financeiros de forma simples.
- Responda em no máximo 3 parágrafos curtos.
"""

# ============ 8. FUNÇÃO PARA CONVERSAR (A "Conversa") ============
def conversar_com_lis(nova_pergunta):
    mensagens_para_ia = [
        {"role": "system", "content": f"{SYSTEM_PROMPT}\n\nCONTEXTO:\n{contexto_dados}"}
    ]
    for msg in st.session_state.historico:
        mensagens_para_ia.append(msg)
    mensagens_para_ia.append({"role": "user", "content": nova_pergunta})
    
    response = client.chat.completions.create(
        model=MODELO,
        messages=mensagens_para_ia,
        max_tokens=500
    )
    return response.choices[0].message.content

# ============ 9. INTERFACE (O "Visual") ============
st.set_page_config(page_title="Lis - Educadora Financeira", layout="centered")
st.title("👩‍🏫 Lis, sua Educadora Financeira")
st.markdown(f"Olá, **{perfil['nome']}**! Como posso te ajudar hoje?")
st.markdown("---")

# Exibe o histórico
for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Campo para digitar a pergunta
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    with st.spinner("Lis está pensando..."):
        resposta = conversar_com_lis(pergunta)
        st.session_state.historico.append({"role": "user", "content": pergunta})
        st.session_state.historico.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.markdown(resposta)

# Botão para limpar a conversa
if st.sidebar.button("Limpar Conversa"):
    st.session_state.historico = []
    st.rerun()
