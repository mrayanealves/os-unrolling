import threading
import numpy
import datetime

lock = threading.Lock() 

# Funcao que recebe duas linhas de uma duas matrizes e as soma
def sumthread (nrow, rowa, rowb):
  global lock
  global result
  aux = []
  
  for i in range(len(rowa)):
    aux.append(rowa[i]+rowb[i])
  
  lock.acquire()
  result.insert(nrow, aux)  
  lock.release()

# Funcao que indica o paralelismo.
def unroll(args, function, method, result):
  if method == "thre":
    a = args[0]
    b = args[1]
    
    threads = []
    row = len(a)    
    
    for i in range(row):  
      threads.insert(i, threading.Thread(target=function, args=(i, a[i], b[i])))
      threads[i].start()


if __name__ == '__main__':
  x = [10, 25, 50, 75, 100, 200, 300, 500, 800]

  for i in range(len(x)):
    a = numpy.random.randint(0, 100 + 1, (x[i], x[i]))
    b = numpy.random.randint(0, 100 + 1, (x[i], x[i]))
    result = []

    args= []
    args.insert(0, a)
    args.insert(1, b)

    start = datetime.datetime.today()

    unroll(args, sumthread, "thre", result)

    end = datetime.datetime.today()

    print(result)

    duracao = end - start
    with open('thread-sum-time.txt', 'a') as file:
      file.write(str(duracao.total_seconds()) + "\n")
      file.close()
    
