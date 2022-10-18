from statistics import mean
import pandas as pd
df = pd.read_csv('/Users/Marcos Rodio/Desktop/Consulta Associado Teste.csv', sep=';', skiprows=1,skipfooter=1, encoding = 'latin')
#print(df)
#Renomeando colunas dentro do dataframe
df = df.rename(columns={"Nascimento":"Nasc."})
'''
print(df.head(15))#Dentro do Head posso passar quantas linhas quero vizualizar
print(df.shape) #Total de linhas e colunas
print(df.columns)#Retorna as colunas do df
print(df.dtypes)#Retorna o tipo de dados do df
print(df.tail(10))#Retona as ultimas linhas do df
print(df.describe())#Dados estatisticos como, media, std desvio padrao, Quartis
print(df["Região"].unique())#Retorna os valores unicos

reg = df.loc[df["Região"] == "VALPARAISO"]#Aplica filtro de coluna
reg1 = df.loc[(df["Região"] == "VALPARAISO" )& (df["Sexo"] == "FEMININO")]#Aplica filtro de coluna o operador & deve ser utilizado para concatenar as condições
print(reg.head(5))
print(reg1.head(10))

print(df.groupby("Região")["Inscrição"].nunique())# contagem distinta Agrupar por região contando as inscrições, primeiro parametro é o agrupador o segundo o objeto de conta gem
print(df.groupby("Região")["Idade"].mean())# Media de idade por região
'''



from statistics import mean
import pandas as pd
df = pd.read_csv('/Users/Marcos Rodio/Desktop/Consulta Associado Teste.csv', sep=';', skiprows=1,skipfooter=1, encoding = 'latin')
#print(df)
#Renomeando colunas dentro do dataframe
df = df.rename(columns={"Nascimento":"Nasc."})
'''
print(df.head(15))#Dentro do Head posso passar quantas linhas quero vizualizar
print(df.shape) #Total de linhas e colunas
print(df.columns)#Retorna as colunas do df
print(df.dtypes)#Retorna o tipo de dados do df
print(df.tail(10))#Retona as ultimas linhas do df
print(df.describe())#Dados estatisticos como, media, std desvio padrao, Quartis
print(df["Região"].unique())#Retorna os valores unicos

reg = df.loc[df["Região"] == "VALPARAISO"]#Aplica filtro de coluna
reg1 = df.loc[(df["Região"] == "VALPARAISO" )& (df["Sexo"] == "FEMININO")]#Aplica filtro de coluna o operador & deve ser utilizado para concatenar as condições
print(reg.head(5))
print(reg1.head(10))

print(df.groupby("Região")["Inscrição"].nunique())# contagem distinta Agrupar por região contando as inscrições, primeiro parametro é o agrupador o segundo o objeto de conta gem
print(df.groupby("Região")["Idade"].mean())# Media de idade por região
'''

