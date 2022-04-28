#!/usr/bin/env python
# coding: utf-8

# ETL - EXTRAÇÃO TRANSFORMAÇÃO E CARGA

# Dados Históricos da B3 - 2020/21/22
# 
# https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/
# 
# Layout Arquivos
# 
# https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

# In[1]:


#importando as bibliotecas - usando a funcao fwf
import pandas as pd


# In[14]:


def read_files(path, name_file, year_date, type_file):
    _file = f'{path}{name_file}{year_date}.{type_file}'
    
    colspecs = [(2,10),
                (10,12),
                (12,24),
                (27,39),
                (56,69),
                (69,82),
                (82,95),
                (108,121),
                (152,170),
                (170,188)           
    ]

    names = ['data_pregao', 'cod_dbi', 'sigla_acao', 'nome_acao',              'preco_abertura', 'preco_maximo', 'preco_minimo', 'preco_fechamento',              'qtd_negociada','volume_total']
    df = pd.read_fwf(_file, colspecs = colspecs, names = names, skiprows = 1)
    
    return df


# In[15]:


#filtrando lote padrão = 2
def filter_stocks(df):
    df = df [df['cod_dbi'] == 2]
    #removendo a coluna 'cod_dbi'
    df = df.drop(['cod_dbi'], 1)
    
    return df


# In[16]:


#ajuste compo de data
def parse_date(df):
    df['data_pregao'] = pd.to_datetime(df['data_pregao'], format= '%Y%m%d')
    return df


# In[17]:


#ajuste dos campos numéricos
def parse_values(df):
    df['preco_abertura'] = (df['preco_abertura'] /100).astype(float)
    df['preco_maximo'] = (df['preco_maximo'] /100).astype(float)
    df['preco_minimo'] = (df['preco_minimo'] /100).astype(float)
    df['preco_fechamento'] = (df['preco_fechamento'] /100).astype(float)
    
    return df


# In[27]:


#juntando os arquivos
def concat_files(path, name_file, year_date, type_file, final_file):
    
    for i, y in enumerate(year_date):
        df = read_files(path, name_file, y, type_file)
        df = filter_stocks(df)
        df = parse_date(df)
        df = parse_values(df)
        
        if i==0:
            df_final = df
        else:
            df_final = pd.concat([df_final, df])
            
    df_final.to_csv(f'{path}//{final_file}', index=False)


# In[28]:


#executando programa de etl

year_date = ['2020', '2021', '2022']

path = f'/home/clayton/Documentos/Projetos/etl_python/data/'

name_file = 'COTAHIST_A'

type_file = 'TXT'

final_file = 'all_bovespa.csv'

concat_files( path, name_file, year_date, type_file, final_file)


# In[ ]:




