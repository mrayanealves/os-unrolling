import pandas as pd
import matplotlib.pyplot as plt

sum_thread = pd.read_csv('files/thread-sum-time.txt', sep="\n", header=None)
sum_seq = pd.read_csv('files/seq-sum-time.txt', sep="\n", header=None)

keys = [10, 25, 50, 75, 100, 200, 300, 500, 800]

plt.plot(keys, 
         sum_thread[0], c='red', label='Threads')
plt.plot(keys, 
         sum_seq[0], c='blue', label='Sequencial')
plt.legend(loc='best')
plt.title('Grafico 1: Comparacao tempo de soma com thread e sequencial')
plt.savefig('graphics/images/sum.png')
plt.show()

mult_thread = pd.read_csv('files/thread-mult-time.txt', sep="\n", header=None)
mult_seq = pd.read_csv('files/seq-mult-time.txt', sep="\n", header=None)

keys = [10, 25, 50, 75, 100, 200, 300]

plt.plot(keys, 
         mult_thread[0], c='red', label='Threads')
plt.plot(keys, 
         mult_seq[0], c='blue', label='Sequencial')
plt.legend(loc='best')
plt.title('Grafico 2: Comparacao tempo de multiplicacao com thread e sequencial')
plt.savefig('graphics/images/mult.png')
plt.show()
