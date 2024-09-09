import pandas as pd

frutas_1 = pd.DataFrame([[30, 20]], columns=['Maça', 'Banana'])
print(frutas_1.head())

frutas_2 = pd.DataFrame([[1000, 700], [5000, 2000]], columns=['Maça', 'Banana'], index=['Vendas 2022', 'Vendas 2023'])
print(frutas_2.head())

fifa_df = pd.read_csv('python-pandas-2/fifa_ranking.csv')

print(fifa_df.head())

# Tipos de dados das colunas
print(fifa_df.info())

# Valores da coluna "previous_points"
print(fifa_df["previous_points"])

# Valor máximo da coluna "previous_points"
print('Máximo:', fifa_df["previous_points"].max())

# Verificar os dados da coluna "previous_points" maiores que 1000
print(fifa_df.loc[fifa_df["previous_points"]>1000])