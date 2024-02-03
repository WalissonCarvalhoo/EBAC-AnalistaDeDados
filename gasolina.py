import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arquivo = '/content/EBAC-AnalistaDeDados/gasolina.csv'

df_gasolina = pd.read_csv(arquivo)

df_gasolina.head()

#Criando o gráfico

sns.lineplot(x='dia', y='venda', data=df_gasolina, marker='o', markersize=7, color='red')
plt.xlabel('Dia de Julho de 2021')
plt.ylabel('Preço')
plt.title('Preço médio da gasolinha em São Paulo')
plt.xticks(df_gasolina['dia'])
plt.grid(True)
plt.savefig('gasolina.png')
plt.show()


