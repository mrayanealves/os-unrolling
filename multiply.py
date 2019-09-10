import threading
import datetime
import numpy

lock = threading.Lock() 

# Funcao recebe uma linha de uma matriz a e uma matriz b e realiza a multiplicacao
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
    
    # Percorre a linha da matrix a (lista)n
    for i in range(len(rowa)):
      # Soma no numero o valor da linha de a com o da coluna em b
      numero += rowa[i]*colb[i] 
    
    # Insere em um vetor auxiliar
    aux.insert(cont, numero)
      
    cont+=1
    numero = 0

  lock.acquire()
  # Insere no resultado na linha nrow recebida o vetor calculado para aquela linha
  result.insert(nrow, aux)
  lock.release()

# Funcao que indica o paralelismo.
def unroll(args, function, method, result):
  if method == "thre":
    a = args[0]
    b = args[1]
    
    threads = []
    
    rowa = len(a)
    
    for i in range(rowa): 
      # Obtem as linhas do vetor a e cria uma thread para o calculo 
      # da multiplicacao dessa linha com a matrix b 
      threads.insert(i, threading.Thread(target=function, args=(i, a[i], b)))
      threads[i].start()

if __name__ == '__main__':
  open('thread-mult-time.txt', 'w').close()

  rangeI = [10, 25, 50, 75, 100, 200, 300]
  
  for i in rangeI:
    a = numpy.random.randint(0, 100 + 1, (i, i))
    b = numpy.random.randint(0, 100 + 1, (i, i))
    result = []

    args = []
    args.insert(0, a)
    args.insert(1, b)

    start = datetime.datetime.today()

    unroll(args, multthread, "thre", result)

    end = datetime.datetime.today()

    with open("thread-mult-time.txt", "a") as file:
      file.write(str((end - start).total_seconds()) + "\n")
      file.close()