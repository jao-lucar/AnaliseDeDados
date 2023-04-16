from Manipulando_arq_csv.Vendas_loja_eletronicos.caminho_vendas import vendas
import pandas as pd
import csv

vendas_df = pd.read_csv(vendas())

media_venda_marca = vendas_df.groupby("marca")["quant_vendida"].mean()

media_venda_marca.to_csv("media_venda_marca.csv")

with open("media_venda_marca.csv") as m:
    leitor = csv.reader(m)
    next(leitor)
    with open("relatorio.txt", "w") as r:
        r.writelines("Média De Venda Por Marca\n" + "=" * 50 + "\n")
        r.writelines(f"{'Marca:':<17}{'Média de Venda':<5} \n")
        for l in leitor:
            a = f"{float(l[1]):.2f}"
            r.writelines(f"{l[0]:<17}{a:>5}%\n")






