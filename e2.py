import pandas as pd

entregas = pd.read_csv("amostra_entregas.csv", sep=';')
print (entregas)

registros, colunas = entregas.shape

print (f"\nRegistros: {registros} | Colunas: {colunas}")

lista_colunas = entregas.columns.tolist()
print(lista_colunas)
