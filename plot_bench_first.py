
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'graph.csv'
x_axis_title = ['Unpending time', 'Ready time', 'Switch time', 'Pending time', 'Total time']

data = pd.read_csv(file_path)
#print(data)
#new_header = data.iloc[0] #grab the first row for the header
#data = data[1:] #take the data less the header row
#data.columns = new_header #set the header row as the df header
print("header", data)
#input()
#input()
print(data.columns.str.strip())
categorias = data['Estados']
print(f"categorias {list(categorias)}")
valor1 = data['Simple linked-list']
valor2 = data['Red/black tree']
valor3 = data['Multi-queue']


x = np.arange(len(categorias))
largura = 0.2
espacamento = 0.10

fig, ax = plt.subplots(figsize=(10, 6))
#print(list(valor1))
valor1 = [int(val) for val in valor1]
valor2 = [int(val) for val in valor2]
valor3 = [int(val) for val in valor3]
barras1 = ax.bar(x - largura - espacamento/2, valor1, largura, label='Simple linked-list')
barras2 = ax.bar(x + largura + espacamento/2, valor2, largura, label='Red/black tree')
barras3 = ax.bar(x , valor3, largura, label='Multi-queue')

#ax.set_title('Current Consumption')
#ax.set_xlabel('Clock Cycles')
ax.set_ylabel('Clock Cycles')
ax.set_xticks(x)
ax.set_xticklabels(list(x_axis_title))
ax.set_ylim(ymin=0)
ax.legend()

def adicionar_valores(barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate(f'{altura}',
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

adicionar_valores(barras1)
adicionar_valores(barras2)
adicionar_valores(barras3)


plt.show()