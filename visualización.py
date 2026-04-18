import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Datos_sucios.csv",sep = ";")
df['nota'] = df['nota'].astype(str).str.replace(",", ".").astype(float)
df = df.dropna(subset=['nota'])
df = df[df['nota'] <= 10]
df['faltas'] = df['faltas'].fillna(0)
df['derecho_beca'] = (df['nota'] >= 8.5) & (df['faltas'] == 0)

# Calculamos la nota media por asignatura

media_por_asignatura = df.groupby("asignatura")["nota"].mean()
media_por_asignatura.plot(kind = "bar", color = ['#4C72B0', '#55A868'])

plt.title("Nota media por asignatura")
plt.xlabel("Asignatura")
plt.ylabel("Nota media")
plt.xticks(rotation = 0)

plt.show()

# Cuántos tienen beca

conteo_becas = df['derecho_beca'].value_counts()
conteo_becas.plot(kind = "pie", autopct='%1.1f%%', labels=['Sin Beca', 'Con Beca'], colors=['#C44E52', '#8172B3'])
plt.ylabel("")

plt.show()