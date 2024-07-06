import pandas as pd

df = pd.read_json('pandas/Alunos.json')

print(df.to_string())
print('informações:', df.info()) # informaçãoes 
print(df.describe()) # descrição 
df.info(show_counts=True, memory_usage=True, verbose=True)

# manipulação de dicionarios:

