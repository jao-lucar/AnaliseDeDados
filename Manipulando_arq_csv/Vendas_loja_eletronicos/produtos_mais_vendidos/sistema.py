from Manipulando_arq_csv.Vendas_loja_eletronicos.caminho_vendas import vendas
import pandas as pd
import csv

vendas_df = pd.read_csv(vendas())

quant_produtos_vendidos_df = pd.DataFrame(vendas_df.groupby("produto")["quant_vendida"].sum())

produtos_mais_vendidos = quant_produtos_vendidos_df.sort_values(by="quant_vendida", ascending=False)

produtos_mais_vendidos.to_csv("produtos_mais_vendidos.csv")

with open("produtos_mais_vendidos.csv") as p:
    leitor = csv.reader(p)
    next(leitor)
    with open("relatorio.txt", "w") as r:
        r.writelines(f"{'Produto':<30}{'Quantidade Vendida':>5}\n")
        for i in leitor:
            x = f"{float(i[1]):.0f}"
            r.writelines(f"{i[0]:<30}{x:>5}\n")



