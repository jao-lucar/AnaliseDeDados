import pandas as pd
def linha():
    print("=" * 100)


dados = pd.read_csv("vendas.csv")
print(dados.head(2)) # mostra as linhas do topo
linha()
print(dados.tail(2)) # mostra as ultimas linhas
linha()
print("shape")
print(dados.shape) # retorna uma tupla com as linhas e colunas
linha()
print("columns")
print(dados.columns)# retorna o nome das colunas
linha()
print("Describe")
print(dados.describe())# retorna algumas conta matematicas das colunas que possuem valores numericos
linha()
print("Info")
print(dados.info()) # retorna informações sobre a quant de linha e coluna, o tipo de dado de cada coluna e a memoria usada
linha()
print("Isnull")
print(dados.isnull()) # retorna o dataframe bolleano, com true pra preenchido com um valor e false pra nulo
linha()
print("dropna")
print(dados.dropna().head(5)) # elimina a linha por completo caso tenha um valor nulo nela
linha()
print("Iloc")
print(dados.iloc[:, 0:2]) # acessa os valores com sua base numerica, sintax = iloc[linha, colunas] ou iloc[linhas, colunas]
linha()
print("loc")
print(dados.loc[:, "data_venda": "marca"]) # acessa os valores com base em rotulos(indices)
linha()
print("value_counts")
print(dados["marca"].value_counts().head(3)) # retorna um series com a quant que cada elemento aparece em uma coluna
linha()
print("groupby")
print(dados.groupby("data_venda")["preco"].sum().head(3)) #junta uma coluna com a outra
linha()
print("sort_values")
print(dados.sort_values(by="quant_vendida")) #organiza o dataframe de acordo com uma coluna
linha()
print("drop")
print(dados.drop([0, 1, 2, 3]).head(3)) # elimina as linhas que se passa como atributo
linha()
print("drop")
print(dados.drop("data_venda", axis=1).tail(3)) # elinima a coluna que se passa como atributo
linha()
print("fillna")
print(dados.fillna("teste").value_counts().head(3)) # preenche todos os valores vazios(nulos) com o parametro passado
linha()
print(dados["preco"].fillna(10.23).astype("int").head(50))
linha()
print(dados["marca"].unique()) #retorna uma lista com os nomes dos valores de uma coluna sem repeti-los
linha()
print(dados["marca"].nunique()) # retorna uma especie de len() do metodo unique
linha()
print("Coor")
colunas_numericas = dados.describe().columns # gambiarra para separar as colunas numericas das não numericas
dados_numericos = dados[colunas_numericas] # continuação da gambiarra
print(dados_numericos.corr())# calcula a coorrelação entre as tabelas
linha()
dados["data_venda"] = pd.to_datetime(dados["data_venda"])
print(pd.pivot_table(dados, values=["preco", "quant_vendida"], index=pd.Grouper(key="data_venda", freq="D"), aggfunc="sum", dropna=True))
linha()