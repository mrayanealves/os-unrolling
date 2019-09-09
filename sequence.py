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
  a = [[4, 6, 5], [5, 8, 9]]
  b = [[3, 2, 1], [5, 9, 6]]
  results = []

  args= []
  args.insert(0, a)
  args.insert(1, b)

  sum(args, results)

  print(results)
  
  results = []

  a = [[4, 8, 4], [1, 3, 1], [1, 2, 4], [1, 1, 1]]
  b = [[3, 2, 4], [5, 9, 4], [5, 9, 4]]

  args = []
  args.insert(0, a)
  args.insert(1, b)

  mult(args, results)

  print(results)