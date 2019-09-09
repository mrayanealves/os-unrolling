import pandas as pd
import matplotlib.pyplot as plt

sum_thread = pd.read_csv('thread-sum-time.txt', sep="\n", header=None)
seq_thread = pd.read_csv('seq-sum-time.txt', sep="\n", header=None)


plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], 
         sum_thread[0], c='green', label='Threads')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], 
         seq_thread[0], c='blue', label='Sequencial')
plt.legend(loc='best')
plt.title('Grafico 1: Comparacao tempo de soma com thread e sequencial')
plt.show()
plt.savefig('sum.png')
