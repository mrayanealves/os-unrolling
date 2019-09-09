import numpy
import datetime

def sum(args, results):
  a = args[0]
  b = args[1]
  
  aux = []
  numero = 0
  
  for i in range(len(a)): 
    aux = []
    for j in range(len(a[0])):
      numero = a[i][j] + b[i][j]
      aux.insert(j, numero)
          
    results.insert(i, aux)

def mult(args, results):
  a = args[0]
  b = args[1]
  
  aux = []
  numero = 0
  
  for i in range(len(a)):
    for j in range(len(b[0])):        
      for k in range(len(b)):
        numero += a[i][k] * b[k][j]
        
      aux.insert(j, numero)
      numero = 0
    
    results.insert(i, aux)
    aux = []

if __name__ == '__main__':
  rangeI = [10, 25, 50, 75, 100, 200, 300, 500, 800]
  
  for i in rangeI:
    a = numpy.random.randint(0, 100 + 1, (i, i))
    b = numpy.random.randint(0, 100 + 1, (i, i))
    results = []

    args= []
    args.insert(0, a)
    args.insert(1, b)

    startSum = datetime.datetime.today()

    sum(args, results)

    endSum = datetime.datetime.today()

    with open("seq-sum-time.txt", "a") as file:
      file.write(str((endSum - startSum).total_seconds()) + "\n")
      file.close()


  rangeI = [10, 25, 50, 75, 100, 200, 300]
  
  for i in rangeI:
    a = numpy.random.randint(0, 100 + 1, (i, i))
    b = numpy.random.randint(0, 100 + 1, (i, i))
    results = []

    args = []
    args.insert(0, a)
    args.insert(1, b)

    startMult = datetime.datetime.today()

    mult(args, results)

    endMult = datetime.datetime.today()
  
    with open("seq-mult-time.txt", "a") as file:
      file.write(str((endMult - startMult).total_seconds()) + "\n")
      file.close()