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



col1, col2, col3 = st.columns(3,vertical_alignment='center')
with col2:
    
    st.button(label='Categorizar dados')



st.markdown("<h3 style='text-align: center; color: black;'>This is an app for personal finance management</h3>", unsafe_allow_html=True)

column1,column2 = st.columns(2,vertical_alignment='top')

with column1:

    st.markdown(f''' 
    <h2 style="background-color: {Cores.VERDE}; 
           padding: 10px; 
           border-radius: 5px; 
           text-align: center;">
    MONEY INFO
    </h2>''', unsafe_allow_html=True)


    
with column2:

    st.markdown(f''' 
    <h2 style="background-color: {Cores.AMARELO}; 
           padding: 10px; 
           border-radius: 5px; 
           text-align: center;">
    DATE INFO
    </h2>''', unsafe_allow_html=True)



with column1:
    
    ##SALDO
    if current_balance > 0: 
        st.markdown(f'''
            Your current balance is $:green[{str(current_balance)}]''')
    elif current_balance == 0: 
        st.markdown(f'''
            Your current balance is $:blue[{str(current_balance)}]''')
    else:
        st.markdown(f'''
            Your current balance is $:red[{str(current_balance)}]''')
        
    st.markdown(f'''Period to Date (PTD) amount $:blue[{str(period_amount)}]''')

    st.markdown(f'''Biggest Debit in a Single Transaction $:red[{str(biggest_debit_amount)}]''')

    st.markdown(f'''Biggest Credit in a Single Transaction $:green[{str(biggest_credit_amount)}]''')   
    
    
with column2:
    
    

    st.markdown(f'''Your last transaction happened in: :blue-background[{last_transaction_date}]''')
    st.markdown(f"Analysed Period: :orange[{period_window}]")

col1, col2, col3 = st.columns(3,vertical_alignment='top')

st.data_editor(Extracted_Data.grouped_df)



st.dataframe(Extracted_Data.sorted_df)

