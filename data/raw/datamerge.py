import pandas as pd
import openpyxl

sp500 = pd.read_csv('data/raw/sp500.csv')[['date', 'close']]
sp500['date'] = pd.to_datetime(sp500['date'])
sp500.rename(columns={'close':'S&P500'}, inplace=True)

ftse = pd.read_csv('data/raw/ftse.csv', sep=';')[['date', 'close']]
ftse['date'] = pd.to_datetime(ftse['date'])
ftse.rename(columns={'close':'FTSE250'},inplace=True)

gold = pd.read_excel('data/raw/Gold_Prices.xlsx', engine='openpyxl', sheet_name='daily_data')
gold.rename(columns={'gold_price':'Gold'},inplace=True)

crude_oil = pd.read_excel('data/raw/crude_oil_price.xlsx', engine='openpyxl', sheet_name='crude_oil')
crude_oil.rename(columns={'Date':'date', 'crude_oil_p_per_barrel':'CrudeOil'},inplace=True)

df_full = gold.merge(crude_oil,on='date').merge(sp500,on='date').merge(ftse,on='date')
df_full.set_index('date', inplace=True)

assert df_full.index.inferred_type == "datetime64"

df_full.to_csv('data/raw/raw_merged.csv', sep=';')