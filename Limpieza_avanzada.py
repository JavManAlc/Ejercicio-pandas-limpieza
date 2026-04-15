import pandas as pd
df = pd.read_csv("Datos_sucios.csv", header = 0, index_col = 0, sep = ";", decimal = ".")
print(df)
print(df.info())


# Como podemos observar tenemos nota como object y tiene que estar como número por lo que lo primero que tenemos que hacer será
# cambiar la coma decimal por un punto

df['nota'] = df['nota'].str.replace(",", ".").astype(float)

# Eliminamos los duplicados

df = df.drop_duplicates()

# Tratamos los nulos

df['faltas'] = df['faltas'].fillna(0)

# Como la nota es una variable importante y no tiene sentido tener registros sin nota

df = df.dropna(subset = 'nota')

# Eliminamos outliers

df = df[df['nota'] <= 10]

# Observamos de nuevo lo que tenemos 

print(df)
print(df.info())

# Vamos con la estadística descriptiva

medias = df.groupby('asignatura')['nota'].mean()
print(medias)

# Creamos una nueva variable

df['der_beca'] = (df['nota'] >= 8.5) & (df['faltas'] == 0)
print(df)