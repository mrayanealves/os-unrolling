# os-unrolling

Utilizando threads para realização de soma e multiplicação de matrizes

### Pre requisitos

1. [Python](https://www.python.org/)

### Informações gerais

A proposta dessa atividade é realizar a soma e a multiplicação de matrizes utilizando threads e fazer um comparativo dessa solução com os algoritmos comuns e sequenciais desses problemas.

### Organização do projeto

* **files**: possui os arquivos .txt que guardam o tempo de execução dos algoritmos de soma de matrizes com threads e sequencial, bem como os de multiplicação de matrizes com threads e sequencial (um arquivo para cada tipo, somando 4 arquivos no total);

* **graphics**: possui o arquivo .py que gera os gráficos comparativos entre as soluções com threads e sequenciais; bem como os arquivos .png com os gráficos gerados;

* **operations**: possui as soluções para soma e multiplicação de matrizes com threads (sum.py e multiply.py, respectivamente) e sequencial (sequence.py). Esses arquivos realizam essas operações e armazenam o tempo de processamento nos arquivos da pasta **files** anteriormente mencionada.

### Executando o projeto

A execução do projeto está direcionada a execução dos arquivos *sum.py*, *multiply.py*, *sequence.py* e *graphics.py*, sendo os três primeiros executados antes do último. 

É importante mencionar que nos arquivos das operações, as matrizes executadas são geradas de forma aleatória de acordo com os tamanhos definidos na lista nomeada de *x* (não por falta de nome melhor) definida no início do método main do *sum.py*, ou *rangeI*, nos arquivos *multiply.py* e *sequence.py*. Esses tamanhos podem ser alterados de acordo com o caso de teste que você queira realizar. Porém, para que a comparação seja justa, certifique-se de que os tamanhos colocados em *x* para *sum.py* sejam os mesmos para *rangeI* na soma em *sequence.py* e a mesma coisa para multiply. Assim, o valor comparado será coerente. Além disso, garanta também que a lista *keys* no arquivo *graphics.py* esteja de acordo com os tamanhos (*x* e *rangeI*) colocados para as somas e multiplicações.
