import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import default_rng


# Simular notas aleatórias para 10 alunos 

alunos = ['Erica','Rodrigo','Thiago','Isabela','Pedro','Andressa','Sandra','Diogo','Fabrício','Gabriel']
alunos.sort()
#print(alunos)

rng = np.random.default_rng()
notas = rng.random(10) * 10
#print(notas)
print(f'Média das notas da turma:{np.round(notas.mean(),2)}')

# Análise dos dados

figura = plt.figure(figsize=(20,15))
figura.suptitle('Distribuição de notas da turma')

plt.subplot(1,2,1)
plt.hist(notas,bins=5,edgecolor='black',color='green',zorder=2,label='Faixa de notas da turma')
plt.legend(fontsize=8)
plt.grid(axis='y',linestyle='--',alpha=0.4,zorder=0)
plt.ylabel('Quantidade de alunos')
plt.xlabel('Nota')

plt.subplot(1,2,2)
plt.boxplot(notas,notch=True,vert=False)
plt.grid(linestyle='--',alpha=0.4,zorder=0)

plt.savefig('distribuicao_notas.png')
plt.show()
