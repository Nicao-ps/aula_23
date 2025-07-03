from datetime import datetime
import pandas as pd
import polars as pl

# 1º Step: Trying to obtain data for analysis
try:
        PATH_DATA = r'../data/'
        
        inicial_hour = datetime.now()
        print('\nLoading data...\n')

        df_january = pd.read_csv(PATH_DATA + '202501_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')
        print(df_january.head())

        df_january = pl.read_csv(PATH_DATA + '202501_NovoBolsaFamilia.csv', separador=';', encoding='iso-8859-1')
        print(df_january.head())

        final_hour = datetime.now()
        print(f'Run time overall: {(final_hour - inicial_hour)}')

except Exception as e:
        print(f'Error while trying to obtain data. {e}')