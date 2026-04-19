# 👩‍🏫 Lis - Sua Educadora Financeira Inteligente

> Projeto desenvolvido para o desafio de IA Generativa da DIO, focado em criar uma experiência personalizada de educação financeira.

## 🌟 O Que é a Lis?

A **Lis** é uma assistente virtual inteligente projetada para transformar a relação das pessoas com o dinheiro. Diferente de uma simples calculadora, a Lis atua como uma educadora: ela analisa seus gastos, ajuda a planejar metas e explica conceitos financeiros complexos de forma simples e amigável.

Este projeto foi personalizado para a usuária **Laura Souza**, utilizando seus dados fictícios para demonstrar como a IA pode oferecer conselhos contextualizados e práticos.

## 🚀 Funcionalidades Principais

- **💬 Chat Interativo:** Compreensão de linguagem natural para tirar dúvidas sobre finanças.
- **🧠 Persistência de Contexto:** A Lis lembra do seu nome e do histórico da conversa.
- **📊 Análise de Gastos:** Identificação automática das maiores categorias de despesas usando Python e Pandas.
- **🔢 Simulações Matemáticas:** Cálculos demonstrativos de tempo para atingir metas de reserva de emergência.
- **🛡️ Segurança e Ética:** Blindagem contra conselhos inadequados e foco exclusivo em educação financeira.
- **📚 Base de Conhecimento:** FAQ integrado sobre produtos financeiros (CDB, Tesouro Selic, FGC, etc).

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3.11](https://www.python.org/)
- **Interface:** [Streamlit](https://streamlit.io/) (Criação de web apps rápidos)
- **Processamento de Dados:** [Pandas](https://pandas.pydata.org/) (Análise de tabelas CSV)
- **IA Generativa:** [OpenAI API](https://openai.com/) (Modelo GPT-4o-mini para o cérebro da assistente)
- **Documentação:** Markdown

## 📁 Estrutura do Projeto

```text
├── data/                          # Base de dados (JSON e CSV)
│   ├── perfil_investidor.json     # Perfil da Laura Souza
│   ├── transacoes.csv             # Histórico de gastos
│   └── produtos_financeiros.json  # Catálogo de produtos
├── docs/                          # Documentação técnica
│   └── PROMPTS_PROJETO.md         # Detalhamento da Engenharia de Prompts
├── src/
│   └── app.py                     # Código principal da aplicação
└── README.md                      # Este manual
```

## 💻 Como Rodar o Projeto no seu VS Code

### 1. Pré-requisitos
Certifique-se de ter o **Python** instalado no seu computador.

### 2. Instalar as Dependências
Abra o terminal no seu VS Code e digite:
```bash
pip install streamlit pandas openai
```

### 3. Configurar a Chave da API
Para a IA funcionar, o projeto utiliza uma chave da OpenAI. (No ambiente de desenvolvimento da Laura, isso já está configurado).

### 4. Executar a Lis
No terminal, dentro da pasta do projeto, digite:
```bash
streamlit run src/app.py
```

## 👩‍💻 Autoria
Projeto adaptado e desenvolvido por **Alice Fraga**, como parte da trilha de IA Generativa da [DIO](https://www.dio.me/).
