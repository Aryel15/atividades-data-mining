import pandas as pd
import json

df_credits = pd.read_csv("python-pandas/tmdb_5000_credits.csv")

print(df_credits.head())
print(df_credits[['title', 'cast']])

for i in range(10):
    cast_list = json.loads(df_credits['cast'][i])

    print(df_credits['title'][i], "|", cast_list[0]['name'])