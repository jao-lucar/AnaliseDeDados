from Manipulando_arq_csv.Vendas_loja_eletronicos.caminho_vendas import vendas
import pandas as pd
import csv

vendas_df = pd.read_csv(vendas())

vendas_df["data_venda"] = pd.to_datetime(vendas_df["data_venda"])
vendas_df["total"] = vendas_df["preco"] * vendas_df["quant_vendida"]
faturamento = vendas_df.groupby(pd.Grouper(key="data_venda", freq="D"))["total"].sum()

faturamento.to_csv("faturamento_diario.csv")

with open("faturamento_diario.csv") as a:
    leitor = csv.reader(a)
    next(leitor)
    with open("relatorio.txt", "w+") as r:
        r.writelines("Faturamento Diário\n")
        r.writelines('=' * 50 + '\n')
        r.writelines(f'{"Data":<20}{"Valor Vendido":<10}\n')
        for linha in leitor:
            r.writelines(f"{linha[0]:<20}R${linha[1]:<10}\n")
