import threading

lock = threading.Lock() 

def multthread(nrow, rowa, b):
  global lock
  global result
  
  numero = 0
  cont = 0
  aux = []
  
  while cont < len(b[0]):
    colb = [(x[cont]) for x in b]
    
    for i in range(len(rowa)):
      numero += rowa[i]*colb[i] 
    
    aux.insert(cont, numero)
      
    cont+=1
    numero = 0
      
  lock.acquire()
  result.insert(nrow, aux)
  lock.release()

def unroll(args, function, method, result):
  if method == "thre":
    a = args[0]
    b = args[1]
    
    threads = []
    
    rowa = len(a)
    
    for i in range(rowa):  
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