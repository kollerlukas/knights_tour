import sys

# sys.setrecursionlimit(10000)

# parameter
n,m = 8,8 # size of the field
s_0 = (1,1) # start point
s_nm = (3,2) # end point

board = {(i+1,j+1) for i in range(n) for j in range(m)} # build board

# return the number of unvisited neighbors of the square si.
def num_neighbors(si,b):
  i,j = si
  neighbors = {(i+1,j+2),(i-1,j+2),(i+1,j-2),(i-1,j-2),(i+2,j+1),(i-2,j+1),(i+2,j-1),(i-2,j-1)}
  return len(neighbors.intersection(b))

# return a list of all valid steps from a square si
def valid_steps(si,b):
  i,j = si
  steps = [(i+1,j+2),(i-1,j+2),(i+1,j-2),(i-1,j-2),(i+2,j+1),(i-2,j+1),(i+2,j-1),(i-2,j-1)]
  valid_steps = [s for s in steps if s in b]
  # sort the valid steps by the number of unvisited neighbors; try to visit worse reachable squares first
  valid_steps = sorted(valid_steps, key=lambda si: num_neighbors(si,b))
  return valid_steps

# recursively compute a path from si to sj using the unvisited squares in b
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

# convert a sequence of squares to a nice matrix representation
def path_to_matrix(n,m,p):
  m = [[0 for _ in range(m)] for _ in range(n)]
  for k, sk in enumerate(p):
    i,j = sk
    m[i-1][j-1] = k+1
  m.reverse() # s.t. (1,1) is the lower-left corner as in (Cull and De Curtains, 1978)
  return m

# compute the paths
p = compute_path(s_0,s_nm,board) 
m = path_to_matrix(n,m,p)
# print result
for r in m:
  print(r)
