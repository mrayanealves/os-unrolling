import threading

lock = threading.Lock() 

# Função que recebe duas linhas de uma duas matrizes e as soma
def sumthread (nrow, rowa, rowb):
  global lock
  global result
  aux = []
  
  for i in range(len(rowa)):
    aux.append(rowa[i]+rowb[i])
  
  lock.acquire()
  result.insert(nrow, aux)  
  lock.release()

# Função que indica o paralelismo.
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
  a = [[1, 2, 5], [5, 8, 9]]
  b = [[3, 2, 1], [5, 9, 6]]
  result = []

  args= []
  args.insert(0, a)
  args.insert(1, b)

  unroll(args, sumthread, "thre", result)

  print(result)