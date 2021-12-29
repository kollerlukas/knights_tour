import sys

sys.setrecursionlimit(10000)

# parameter
n,m = 50,50
s_0 = (1,1)
s_nm = (3,2)

board = {(i+1,j+1) for i in range(n) for j in range(m)}

def num_neighbours(si,b):
  i,j = si
  neighbours = {(i+1,j+2),(i-1,j+2),(i+1,j-2),(i-1,j-2),(i+2,j+1),(i-2,j+1),(i+2,j-1),(i-2,j-1)}
  return len(neighbours.intersection(b))

def valid_steps(si,b):
  i,j = si
  steps = [(i+1,j+2),(i-1,j+2),(i+1,j-2),(i-1,j-2),(i+2,j+1),(i-2,j+1),(i+2,j-1),(i-2,j-1)]
  valid_steps = [s for s in steps if s in b]
  valid_steps = sorted(valid_steps, key=lambda si: num_neighbours(si,b))
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

p = compute_path(s_0,s_nm,board) 
print(p)
