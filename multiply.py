import threading

lock = threading.Lock() 

# Função recebe uma linha de uma matriz a e uma matriz b e realiza a multiplicação
def multthread(nrow, rowa, b):
  global lock
  global result
  
  numero = 0
  cont = 0
  aux = []
  
  # Enquanto o contador for menor que a quantidade de elementos na coluna de b
  while cont < len(b[0]):
    # Cria uma lista com os elementos de uma coluna de b
    colb = [(x[cont]) for x in b]
    
    # Percorre a linha da matrix a (lista)
    for i in range(len(rowa)):
      # Soma no número o valor da linha de a com o da coluna em b
      numero += rowa[i]*colb[i] 
    
    # Insere em um vetor auxiliar
    aux.insert(cont, numero)
      
    cont+=1
    numero = 0

  lock.acquire()
  # Insere no resultado na linha nrow recebida o vetor calculado para aquela linha
  result.insert(nrow, aux)
  lock.release()

# Função que indica o paralelismo.
def unroll(args, function, method, result):
  if method == "thre":
    a = args[0]
    b = args[1]
    
    threads = []
    
    rowa = len(a)
    
    for i in range(rowa): 
      # Obtém as linhas do vetor a e cria uma thread para o cálculo 
      # da múltiplicação dessa linha com a matrix b 
      threads.insert(i, threading.Thread(target=function, args=(i, a[i], b)))
      threads[i].start()

if __name__ == '__main__':
    result = []

    a = [[4, 8, 4], [1, 3, 1], [1, 2, 4], [1, 1, 1]]
    b = [[3, 2, 4], [5, 9, 4], [5, 9, 4]]

    args = []
    args.insert(0, a)
    args.insert(1, b)

    unroll(args, multthread, "thre", result)

    print(result)