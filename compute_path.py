import sys

# sys.setrecursionlimit(10000)

# parameter
n,m = 8,8
s_0 = (1,1)
s_nm = (3,2)

board = {(i+1,j+1) for i in range(n) for j in range(m)}

def num_neighbors(si,b):
  i,j = si
  neighbors = {(i+1,j+2),(i-1,j+2),(i+1,j-2),(i-1,j-2),(i+2,j+1),(i-2,j+1),(i+2,j-1),(i-2,j-1)}
  return len(neighbors.intersection(b))

def valid_steps(si,b):
  i,j = si
  steps = [(i+1,j+2),(i-1,j+2),(i+1,j-2),(i-1,j-2),(i+2,j+1),(i-2,j+1),(i+2,j-1),(i-2,j-1)]
  valid_steps = [s for s in steps if s in b]
  valid_steps = sorted(valid_steps, key=lambda si: num_neighbors(si,b))
  return valid_steps

def compute_path(si,sj,b):
  if b == {} or not si in b or not sj in b:
    return None
  elif b == {si} and si == sj:
    return [si]
  else:
    for s in valid_steps(si,b):
      p = compute_path(sj,s,b-{si})
      if not p is None:
        p.append(si)
        p.reverse()
        return p
    return None

def path_to_matrix(n,m,p):
  m = [[0 for _ in range(m)] for _ in range(n)]
  for k, sk in enumerate(p):
    i,j = sk
    m[i-1][j-1] = k+1
  return m

p = compute_path(s_0,s_nm,board) 
m = path_to_matrix(n,m,p)
for r in m:
  print(r)
