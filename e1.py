import pandas as pd

entregas = pd.DataFrame({
    "Entrega_ID": [
        "E101", "E102", "E103", "E104",
        "E105", "E106", "E107", "E108"
    ],
    "Origem": [
        "Brasília", "Goiânia", "Anápolis", "Brasília",
        "Uberlândia", "Goiânia", "Brasília", "Anápolis"
    ],
    "Destino": [
        "Goiânia", "Brasília", "Brasília", "São Paulo",
        "Brasília", "Anápolis", "Uberlândia", "Goiânia"
    ],
    "Distancia_km": [210, 210, 160, 1010, 420, 55, 420, 55],
    "Peso_kg": [800, 1200, None, 3500, 1800, 400, 2200, 650],
    "Tempo_h": [4.0, 4.5, 3.0, 18.0, None, 1.5, 7.0, 1.8],
    "Modal": ["Rodoviário"] * 8,
})

print("\nPRIMEIROS REGISTROS:\n")
print (entregas.head(4))

print("\nÚLTIMOS REGISTROS:\n")
print (entregas.tail(2))

registros, colunas = entregas.shape

print (f"\nRegistros : {registros} | Colunas : {colunas}.")

print (f"Colunas : {entregas.columns.tolist()}")

print("\nTIPOS DAS COLUNAS:\n")
print(entregas.dtypes)

print("\nESTRUTURA E PREENCHIMENTO:\n")
entregas.info()

df = entregas[["Entrega_ID", "Distancia_km", "Tempo_h"]]

print ("\nCOLUNAS SELECIONADAS:\n")
print(df)
