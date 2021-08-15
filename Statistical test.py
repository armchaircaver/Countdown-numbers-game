from Countdown import countallexpressions,counttargets
from random import randint as RI
from statistics import mean, median, variance, stdev
from itertools import combinations

def printstats(counts):
    m = mean(counts)
    med = median(counts)
    sd = stdev(counts)
    print("mean:",m,", median:",int(med),", st dev:",round(sd,1))
    print("minimum:",min(counts), ",maximum:",max(counts))


print("Test random combinations of 2 top + 4 bottom - all expressions")
top2 = [ x for x in combinations([25,50,75,100],2)]
bottom4 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),4)]
counts=[]

for _ in range(100):
    A= list(top2[RI(0,len(top2)-1)] + bottom4[RI(0,len(bottom4)-1)])
    c = countallexpressions(A)
    counts.append(c)

printstats(counts)

print("Test random combinations of 1 top + 5 bottom - all expressions")
bottom5 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),5)]
counts=[]

for _ in range(100):
    A=[RI(1,4)*25]+ list(bottom5[RI(0,len(bottom5)-1)])
    c = countallexpressions(A)
    counts.append(c)        

printstats(counts)

print("\nTest random combinations of 2 top + 4 bottom")
top2 = [ x for x in combinations([25,50,75,100],2)]
bottom4 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),4)]
print( "cards\ttargets\texpressions\texp/target")
for _ in range(10):
  A= list(top2[RI(0,len(top2)-1)] + bottom4[RI(0,len(bottom4)-1)])
  c,n = counttargets(A)
  print(A,"\t", n ,"\t",c,"\t",round(c/n,1))          

print("\nTest random combinations of 1 top + 5 bottom")
bottom5 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),5)]
print( "cards\ttargets\texpressions\texp/target")
for _ in range(10):
  A=[RI(1,4)*25]+ list(bottom5[RI(0,len(bottom5)-1)])
  c,n = counttargets(A)
  print(A,"\t", n ,"\t",c,"\t",round(c/n,1))          

print("\nTest random combinations of 2 top + 4 bottom - all expressions")
top2 = [ x for x in combinations([25,50,75,100],2)]
bottom4 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),4)]
print( "cards\ttargets")
for _ in range(10):
  A= list(top2[RI(0,len(top2)-1)] + bottom4[RI(0,len(bottom4)-1)])
  c = countallexpressions(A)
  print(A,"\t",c)          

print("\nTest random combinations of 1 top + 5 bottom - all expressions")
bottom5 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),5)]
print( "cards\ttargets")
for _ in range(10):
  A=[RI(1,4)*25]+ list(bottom5[RI(0,len(bottom5)-1)])
  c = countallexpressions(A)
  print(A,"\t",c)          

"""
from run with samples of 100

Test random combinations of 2 top + 4 bottom - all expressions
mean: 58451.15 , median: 50650 , st dev: 21933.5
minimum: 15046 ,maximum: 110308

Test random combinations of 1 top + 5 bottom - all expressions
mean: 51877.96 , median: 47105 , st dev: 21859.7
minimum: 9461 ,maximum: 125137

"""
