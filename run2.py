import statistics 

def valid_walks(d, n, m):
  current=[[]]
  for i in range(d):
    temp=[]
    for j in range(n):
      for k in current:
        temp.append(k+[j])
    current=temp
  res=[]
  k = {}
  for c in current:
    res.append(helper(c, d, n, m, k))
  return statistics.mean(res)

def helper(current_point, d, n, m, k):
  if m==0:
    return 1
  if str(current_point) + "|" + str(m) in k:
      return k[str(current_point) + "|" + str(m)]
  result = 0
  for i in possible_ways_counter(current_point, n):
    result += helper(i, d, n, m-1, k)
  k[str(current_point) + "|" + str(m)] = result
  return result

def possible_ways_counter(current_point,n):
  ways=[]
  for i in range(len(current_point)):
    if current_point[i]==0:
      ways.append(current_point[:i]+ [current_point[i]+1] + current_point[i+1:])
    elif current_point[i]==n-1:
      ways.append(current_point[:i]+ [current_point[i]-1] + current_point[i+1:])
    else:
      ways.append(current_point[:i]+ [current_point[i]+1] + current_point[i+1:])
      ways.append(current_point[:i]+ [current_point[i]-1] + current_point[i+1:])
  return ways

d=4
n=10
m=10
print valid_walks(d, n, m)