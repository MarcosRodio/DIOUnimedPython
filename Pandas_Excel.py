<<<<<<< HEAD
from encodings.utf_8 import encode
import pandas as pd
import matplotlib.pyplot as plt



df1 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Araçatuba.xlsx', engine='openpyxl')
df2 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Andradina.xlsx', engine='openpyxl')
df3 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Birigui.xlsx', engine='openpyxl')
df4 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Valparaiso.xlsx', engine='openpyxl')

print(df1.head(5))
print(df2.head(5))
print(df3.head(5))
print(df4.head(5))

#juntando as bases

df = pd.concat([df1,df2,df3,df4])
'''
print(df.head(5))#5 primeiras linhas
print('------------------------------------------------------')
print(df.tail(5))#5 ultimas linhas
print('------------------------------------------------------')
print(df.dtypes)#verificar tipo de dado de cada coluna
print(df.sample(10))#pegar amostra
df['Loja ID'] = df['Loja ID'].astype("object")
print(df)
print(df.dtypes)#verificar tipo de dado de cada coluna

print(df.isnull().sum())#Verificando valores nulos

#substituindo valores nulos pela media
df['vendas'].fillna(df['vendas'].mean(), inplace=True)
#substituindo valor nulos por 0
df['vendas'].fillna(0, inplace=True)
#apagando as linhas com valores nulos
df.dropna(implace=True)
#apagando as linhas com valores nulos com base em apenas 1 coluna
df.dropna(subset=["vendas"], inplace=True)
#apagando as linhas com valores faltantes em todas as linhas 
df.dropna(how='all', inplace=True)

#criando colunas novas (receita)
df["Receita"] = df["Vendas"].mul(df['Qtde'])
print(df.head())
#df["Receita/Vendas"] = df["Receita"] / df{"Vendas"}

#Retornando a maior receita
print('---------------------------------------------------------')
print('Maior Receita', df['Receita'].max())
print('Menor Receita', df['Receita'].min())
print('---------------------------------------------------------')
print('2 Maiores Receitas')
print(df.nlargest(2,['Receita']))
print('---------------------------------------------------------')
print('2 Menores Receitas')
print(df.nsmallest(2,['Receita']))

print('---------------------------------------------------------')
print('Agrupamento por cidade retornando soma das receitas')
print(df.groupby('Cidade')['Receita'].sum())

#Ordenando Dados
print('---------------------------------------------------------')
print(df.sort_values("Receita", ascending=False).head(10))
'''
#Trabalhando Com Datas

print("Converter types int/float/object em data")
print(df.dtypes)
#df['Data'] = df['Data'].astype("Int64") converte para int
df['Data'] = pd.to_datetime(df['Data'])
print('---------------------------------------------------------')
print("Agrupando por ano")
print(df.groupby(df['Data'].dt.year)['Vendas'].sum())
print('---------------------------------------------------------')
print("Criando uma nova coluna com o ano")
df["Ano_Venda"]= df["Data"].dt.year
print(df.sample(5))
print('---------------------------------------------------------')
print("Extraindo o mês e o dia")
df["Mes_Venda"], df["Dia_Venda"] = (df["Data"].dt.month, df["Data"].dt.day)
print(df.sample(5))
print('---------------------------------------------------------')
print("Calculando a diferença de dias")
df["Diferença_Dias"] = df["Data"] - df["Data"].min()
print(df)
print('---------------------------------------------------------')
print("Criando a Coluna de Trimestre")
df["Trimestre_Venda"] = df["Data"].dt.quarter
print(df)
print('---------------------------------------------------------')
print("Filtrando as vendas de Fevereiro")
vendas_fevereiro_22 = df.loc[(df["Data"].dt.year== 2022) & (df["Data"].dt.month==2)]
print(vendas_fevereiro_22)
#Contagem de vendas por loja
print(df["Loja ID"].value_counts(ascending=False))

#Grafico de Barras
df["Loja ID"].value_counts().plot.bar()



=======
from encodings.utf_8 import encode
import pandas as pd
import matplotlib.pyplot as plt



df1 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Araçatuba.xlsx', engine='openpyxl')
df2 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Andradina.xlsx', engine='openpyxl')
df3 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Birigui.xlsx', engine='openpyxl')
df4 = pd.read_excel('/Users/Marcos Rodio/Desktop/base_vendas/Valparaiso.xlsx', engine='openpyxl')

print(df1.head(5))
print(df2.head(5))
print(df3.head(5))
print(df4.head(5))

#juntando as bases

df = pd.concat([df1,df2,df3,df4])
'''
print(df.head(5))#5 primeiras linhas
print('------------------------------------------------------')
print(df.tail(5))#5 ultimas linhas
print('------------------------------------------------------')
print(df.dtypes)#verificar tipo de dado de cada coluna
print(df.sample(10))#pegar amostra
df['Loja ID'] = df['Loja ID'].astype("object")
print(df)
print(df.dtypes)#verificar tipo de dado de cada coluna

print(df.isnull().sum())#Verificando valores nulos

#substituindo valores nulos pela media
df['vendas'].fillna(df['vendas'].mean(), inplace=True)
#substituindo valor nulos por 0
df['vendas'].fillna(0, inplace=True)
#apagando as linhas com valores nulos
df.dropna(implace=True)
#apagando as linhas com valores nulos com base em apenas 1 coluna
df.dropna(subset=["vendas"], inplace=True)
#apagando as linhas com valores faltantes em todas as linhas 
df.dropna(how='all', inplace=True)

#criando colunas novas (receita)
df["Receita"] = df["Vendas"].mul(df['Qtde'])
print(df.head())
#df["Receita/Vendas"] = df["Receita"] / df{"Vendas"}

#Retornando a maior receita
print('---------------------------------------------------------')
print('Maior Receita', df['Receita'].max())
print('Menor Receita', df['Receita'].min())
print('---------------------------------------------------------')
print('2 Maiores Receitas')
print(df.nlargest(2,['Receita']))
print('---------------------------------------------------------')
print('2 Menores Receitas')
print(df.nsmallest(2,['Receita']))

print('---------------------------------------------------------')
print('Agrupamento por cidade retornando soma das receitas')
print(df.groupby('Cidade')['Receita'].sum())

#Ordenando Dados
print('---------------------------------------------------------')
print(df.sort_values("Receita", ascending=False).head(10))
'''
#Trabalhando Com Datas

print("Converter types int/float/object em data")
print(df.dtypes)
#df['Data'] = df['Data'].astype("Int64") converte para int
df['Data'] = pd.to_datetime(df['Data'])
print('---------------------------------------------------------')
print("Agrupando por ano")
print(df.groupby(df['Data'].dt.year)['Vendas'].sum())
print('---------------------------------------------------------')
print("Criando uma nova coluna com o ano")
df["Ano_Venda"]= df["Data"].dt.year
print(df.sample(5))
print('---------------------------------------------------------')
print("Extraindo o mês e o dia")
df["Mes_Venda"], df["Dia_Venda"] = (df["Data"].dt.month, df["Data"].dt.day)
print(df.sample(5))
print('---------------------------------------------------------')
print("Calculando a diferença de dias")
df["Diferença_Dias"] = df["Data"] - df["Data"].min()
print(df)
print('---------------------------------------------------------')
print("Criando a Coluna de Trimestre")
df["Trimestre_Venda"] = df["Data"].dt.quarter
print(df)
print('---------------------------------------------------------')
print("Filtrando as vendas de Fevereiro")
vendas_fevereiro_22 = df.loc[(df["Data"].dt.year== 2022) & (df["Data"].dt.month==2)]
print(vendas_fevereiro_22)
#Contagem de vendas por loja
print(df["Loja ID"].value_counts(ascending=False))

#Grafico de Barras
df["Loja ID"].value_counts().plot.bar()



>>>>>>> 42bbfde (Commit_1)
