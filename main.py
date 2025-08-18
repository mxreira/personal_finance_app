import streamlit as st
import numpy as np
import pandas as pd
import os
from data_extractor import Extracted_Data
from ux import Cores



current_balance = Extracted_Data.current_balance
last_transaction_date = Extracted_Data.last_transaction_date
period_window = Extracted_Data.period_window
period_amount = Extracted_Data.period_amount

biggest_debit_amount = Extracted_Data.biggest_debit_amount
biggest_debit_counterparty = Extracted_Data.biggest_debit_counterparty


biggest_credit_amount = Extracted_Data.biggest_credit_amount
biggest_credit_counterparty = Extracted_Data.biggest_credit_counterparty

most_transactions_date_count = Extracted_Data.most_transactions_date_count
most_transactions_date_date = Extracted_Data.most_transactions_date_date

st.set_page_config(page_title="PFM", layout="wide")

# --- Estado global (NÃO sobrescreva depois) ---
st.session_state.setdefault("username", "Anônimo")
# ---------- Router helpers ----------
PAGES = {}

def page(label):
    def wrapper(fn):
        PAGES[label] = fn
        return fn
    return wrapper

def sync_nav(default="Dashboard"):
    # 1) lê da URL
    url_page = st.query_params.get("page", [default])[0] if hasattr(st, "query_params") else default
    # 2) inicializa estado
    if "nav" not in st.session_state:
        st.session_state.nav = url_page
    # 3) sidebar (escolha do usuário)
    # Conteúdo da barra lateral (ocupa toda a altura automaticamente)
    with st.sidebar:
        st.markdown(f"#### Seja bem vindo, {st.session_state.username}")
        st.markdown("## Menu")
        st.session_state.nav = st.radio(
            "Navegação",
            list(PAGES.keys()),
            index=list(PAGES.keys()).index(st.session_state.nav) if st.session_state.nav in PAGES else 0,
            label_visibility="collapsed",
            key="nav_radio"
        )
    # 4) grava na URL (para compartilhar/atualizar a página atual)
    try:
        st.query_params["page"] = st.session_state.nav
    except Exception:
        pass
    return st.session_state.nav

# ---------- Páginas ----------
@page("Dashboard")
def render_dashboard():
    st.header("Dashboard")
    st.write("KPIs, cards, gráficos…")
    col1, col2, col3 = st.columns(3,vertical_alignment='center')
    with col2:
        
        st.button(label='Categorizar dados')



    st.markdown("<h3 style='text-align: center; color: black;'>This is an app for personal finance management</h3>", unsafe_allow_html=True)

    column1,column2 = st.columns(2,vertical_alignment='top')




    with column1:
        st.markdown(f'''
                        <div style="background-color:{Cores.CINZA_30}; border-radius:12px; overflow:hidden;">

    <!-- HEADER -->
    <div style="
        background-color:{Cores.VERDE};   /* verde mais forte */
        color:white;
        font-weight:800;
        font-size:1.4rem;
        text-align:center;
        padding:8px;">
        MONEY INFO
    </div>

    <!-- BODY -->
    <div style="padding:16px;">
        <p>Your current balance: <span style="color:red;">${current_balance}</span></p>
        <p>Period to Date (PTD) amount: <span style="color:blue;">${period_amount}</span></p>
        <p>Biggest Debit in a single transaction: <span style="color:red;">${biggest_debit_amount}</span></p>
        <p>Biggest Credit in a single transaction: <span style="color:green;">${biggest_credit_amount}</span></p>
    </div>

    </div>

    ''', unsafe_allow_html= True)
        
    with column2:
        st.markdown(f'''
                        <div style="background-color:{Cores.CINZA_30}; border-radius:12px; overflow:hidden;">

    <!-- HEADER -->
    <div style="
        background-color:{Cores.AMARELO};   /* verde mais forte */
        color:white;
        font-weight:800;
        font-size:1.4rem;
        text-align:center;
        padding:8px;">
        DATE INFO
    </div>

    <!-- BODY -->
    <div style="padding:16px;">
        <p>Your last transaction happened in: <span style="background-color:{Cores.AMARELO_CLARO};">{last_transaction_date}</span></p>
        <p>Analyzed Period: <span style="background-color:{Cores.AMARELO_CLARO};">{period_window}</span></p>
        <p>Date with most transactions: <span style="background-color:{Cores.AMARELO_CLARO};">{most_transactions_date_date}</span></p>
        <p>Count of transactions in {most_transactions_date_date}: <span style="background-color:{Cores.AMARELO_CLARO};">{most_transactions_date_count}</span></p>
    </div>

    </div>

    ''', unsafe_allow_html= True)
        
    st.header('TOP 5 Counterparties in amount spent')
    st.bar_chart(data= Extracted_Data.top_5_outcome_counterparties_df,x="counterparty",x_label="Counterparties",y="amount",y_label='Amount in USD',color="counterparty")

    st.header('TOP 5 Counterparties in amount received')
    st.bar_chart(data= Extracted_Data.top_5_income_counterparties_df,x="counterparty", x_label="Counterparties",y="amount",y_label='Amount in USD',color="counterparty")

@page("Transações")
def render_transacoes():
    st.header("Transações")
    
    st.header('Amount per counterparty')    
    st.dataframe(Extracted_Data.grouped_df)


    st.header('Sorted Dataframe by amount')
    st.dataframe(Extracted_Data.sorted_df)

@page("Configurações")
def render_config():
    
    st.header("Configurações")
    st.toggle("Tema escuro", key="cfg_dark")
    # atualização imediata (sem botão)
    st.text_input("Nome do perfil", key="username")
    

# ---------- Execução ----------
current = sync_nav(default="Dashboard")
PAGES[current]()   # chama a função da página selecionada

# Estilo opcional da sidebar (cor, borda, largura aproximada)
st.markdown(f"""
<style>
/* fundo e borda da sidebar */
section[data-testid="stSidebar"] {{
    background-color: {getattr(Cores, 'CINZA_F5', '#F5F5F5')};
    border-right: 1px solid {getattr(Cores, 'CINZA_CLARO', '#D3D3D3')};
}}
/* “largura” visual (Streamlit não expõe API; esse padding amplia a área útil) */
section[data-testid="stSidebar"] .css-1d391kg, 
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
    padding-right: 18px;
}}
</style>
""", unsafe_allow_html=True)













