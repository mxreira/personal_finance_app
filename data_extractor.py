import pandas as pd
from datetime import datetime

df = pd.read_csv(r'C:\Users\Gabriel\Documents\Main_Python\new\personal_finance_app\bd\extrato_bancario_base.csv')

df_counterparty = df[['counterparty','amount']]
grouped_df = df_counterparty.groupby('counterparty').sum()
sorted_df = df.sort_values('amount',ascending=True)

descricoes = df['description']

most_commom_counterparty = df['counterparty'].mode()[0]

biggest_credit_amount = float(sorted_df.iloc[-1].amount)
biggest_credit_counterparty = str(sorted_df.iloc[-1].counterparty)

biggest_debit_amount = float(sorted_df.iloc[0].amount)
biggest_debit_counterparty = str(sorted_df.iloc[0].counterparty)


class Extracted_Data:
    df
    df_counterparty = df[['counterparty','amount']]
    grouped_df = df_counterparty.groupby('counterparty').sum().sort_values('amount',ascending=True)
    sorted_df = df.sort_values('amount',ascending=True)
    date_sorted_df = df.sort_values('date',ascending=True)
    
    first_transaction_date = pd.to_datetime(date_sorted_df['date'].iloc[0])
    last_transaction_date = pd.to_datetime(date_sorted_df['date'].iloc[-1])
    
    period_window = last_transaction_date - first_transaction_date
    
    descricoes = df['description']

    most_commom_counterparty = df['counterparty'].mode()[0]

    biggest_credit_amount = float(sorted_df.iloc[-1].amount)
    biggest_credit_counterparty = str(sorted_df.iloc[-1].counterparty)

    biggest_debit_amount = float(sorted_df.iloc[0].amount)
    biggest_debit_counterparty = str(sorted_df.iloc[0].counterparty)

        
    period_amount = df['amount'].sum()

    current_balance = float(df['running_balance'].iloc[-1])

    