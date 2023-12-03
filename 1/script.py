import re

sum=0
with open('input.txt','r') as f:
  for line in f:
    m = re.search('\d',line)
    n = re.search('\d',line[::-1])
    sum+=(int(m.group(0)+n.group(0)))

print(sum)
