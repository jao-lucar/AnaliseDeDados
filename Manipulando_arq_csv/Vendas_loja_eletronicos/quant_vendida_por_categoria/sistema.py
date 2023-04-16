from Manipulando_arq_csv.Vendas_loja_eletronicos.caminho_vendas import vendas
import pandas as pd
import csv

vendas_df = pd.read_csv(vendas())


vendas_df["quant_vendida"] = vendas_df["quant_vendida"].fillna(0)

vendas_df["quant_vendida"] = vendas_df["quant_vendida"].astype("int")
quant_vendida_categoria = vendas_df.groupby("categoria")["quant_vendida"].sum()
quant_vendida_categoria.to_csv("quant_vendida_categoria.csv")


with open("quant_vendida_categoria.csv") as q:
    leitor = csv.reader(q)
    next(leitor)
    with open("relatorio.txt", 'w') as r:
        r.writelines("Quantidade Vendida Por Categoria\n")
        r.writelines('=' * 100 + '\n')
        r.writelines(f"{'Categoria':<25}{'Quant_vendida':<10}\n")
        for i in leitor:
            r.writelines(f"{i[0]:<25}{i[1]:<10}\n")
