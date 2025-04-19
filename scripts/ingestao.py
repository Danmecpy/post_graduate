import duckdb
import pandas as pd
import os
from datetime import datetime

con = duckdb.connect(database='dados_duckdb.db', read_only=False)


arquivo = 'z0019_2.csv'
data_ingestao = datetime.now()
df = pd.read_csv(f'../landing/{arquivo}', sep = ';')
df['nome_arquivo'] = arquivo
df['data_ingestao'] = data_ingestao
df.head()

con.execute("""
            CREATE TABLE IF NOT EXISTS  bronze_produtos(
                NATBR VARCHAR,
                MAKTX VARCHAR,
                WERKS VARCHAR,
                MAINST VARCHAR,
                LABST VARCHAR,
                nome_arquivo VARCHAR,
                data_ingestao TIMESTAMP
            )
""")


con.execute("INSERT INTO bronze_produtos SELECT * FROM df")
resultado = con.execute("SELECT * FROM bronze_produtos").fetchdf()
resultado.head(6)
con.close()