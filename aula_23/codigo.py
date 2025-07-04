from datetime import datetime
import pandas as pd
import polars as pl

# 1º Step: Trying to obtain data for analysis
try:
        PATH_DATA = r'../data/'
        
        inicial_hour = datetime.now()
        
        print('\nLoading data...')

        archives_list = ['202501_NovoBolsaFamilia.csv',
                         '202502_NovoBolsaFamilia.csv',
                         '202503_NovoBolsaFamilia.csv',
                         '202504_NovoBolsaFamilia.csv',
                         '202505_NovoBolsaFamilia.csv']

        df_bolsa_familia = None

        for archive in archives_list:
                print(f'\nWorking with archive {archive}\n')
                
                # df = pd.read_csv(PATH_DATA + archive, sep=';', encoding='iso-8859-1')
                df = pl.read_csv(PATH_DATA + archive, separator=';', encoding='iso-8859-1')

                if df_bolsa_familia is None:
                        df_bolsa_familia = df
                else:
                        # df_bolsa_familia = pd.concat([df_bolsa_familia, df])
                        df_bolsa_familia = pl.concat([df_bolsa_familia, df])

                print(df)
                print(df.shape)

                del df

        print('Bolsa Família Concatenado')
        print(df_bolsa_familia.head())
        print(df_bolsa_familia.shape)
        
        final_hour = datetime.now()

        print(f'Run time overall: {(final_hour - inicial_hour)}')

except Exception as e:
        print(f'Error while trying to obtain data. {e}')
