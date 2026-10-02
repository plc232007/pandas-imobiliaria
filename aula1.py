import pandas as pd

entregas = pd.DataFrame ({
    "Identificador": ["E001", "E002", "E003", "E004"],
    "Origem": ["Brásilia", "Goiânia","Brasília", "Anápolis"],
    "Distância_km": [210, 180, 950, 160],
    "Peso_kg": [800, 1200, 2500, 600],
    "Tempo_h": [4.0, None, 15.0, 3.5],
})

print ("\nPRIMEIROS REGISTROS")
print (entregas.head(2))

linhas, colunas = entregas.shape

print ("\nDIMENSÕES")
print (f"{linhas} registros e {colunas} colunas.")


