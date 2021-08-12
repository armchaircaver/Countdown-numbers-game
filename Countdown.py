# -*- coding: cp1252 -*-
from itertools import combinations

def wrap(t, condition=True):
    return ''.join(["(",t,")"]) if condition else t

#@profile
def expressions( A, processed=set() ):
  # initially, A is an array of numbers
  # In recursive calls, A is an array of tuples (n,t,o,x,y) where n in a number,
  # t is a text expression of n, o is the last operation applied to x,y to produce n = xoy

  if type(A[0])==int: # inital call, so convert to array of tuples
    A = [ (A[i],str(A[i]),"",0,0) for i in range(len(A))]
    processed=set()
  else: # recursive call, so return the expression formed in the parent
    n,t,o,x,y = A[0]
    if (n,t) not in processed:
      yield A[0]
      processed.add( (n,t) )

  A.sort()
  #print len(A), [(x,t) for x,t,o,a,b in A]
  tA=tuple(A)
  if tA in processed:
    return
  processed.add(tA)

  if A[0][0]==0:
    return
  
  for p1, p2 in combinations(range(len(A)),2):

    p1,p2 = sorted((p1,p2))
    
    n1,t1,o1,x1,y1 = A[p1]
    n2,t2,o2,x2,y2 = A[p2]

    # construct B, a copy of A without the 2 selected items
    B= A[:]
    B.pop(p2)
    B.pop(p1)

    # don't process x/(y/z) as (x*z)/y produces the same answer
    # don't process x/(y*z) as x/y/z produces the same answer
    if n2 != 0 and n2 != 1 and n1%n2==0 and o2 not in ('*','/'):
      C=[(n1//n2, wrap(t1,o1 not in ('',))+ '�' +wrap(t2,o2!=''),"/",n1,n2)]
      for x in expressions(C+B, processed):
        yield x
      
    if n1 != 0 and n2%n1==0 and o1 not in ('*','/') and n1!=1:
      C=[(n2//n1, wrap(t2,o2 not in ('',))+'�'+wrap(t1, o1!=''),"/",n2,n1)]
      for x in expressions(C+B, processed):
        yield x

    # don't process x*(y/z), as (x*y)/z produces the same answer
    # don't process (x/y)*z as (x*z)/y produces the same answer
    if o2!='/' and o1!='/' and n2!=1 and n1!=1:
      # don't process x*(y*z) if (x>y or x>z)
      if not(o2=='*' and (n1>x2 or n1>y2)):
        C = [(n1*n2,wrap(t1,o1 not in ('','*'))+'�'+wrap(t2,o2 not in ('','*')),"*",n1,n2)]
        for x in expressions(C+B, processed):
          yield x

    # don't process x-(y-z), as x+y-z produces the same answer
    # don't process x-(y+z), as x-y-z produces the same answer
    # don't process (x-y)-z if  y>z.  x-z-y produces the same answer
    if n1>=n2:
      if o2 not in ('+','-'):
        if not( o1=='-' and y1>n2):
          C=[(n1-n2,wrap(t1,False)+"-"+wrap(t2,o2 not in ('','*','/')),"-",n1,n2)]
          for x in expressions(C+B, processed):
            yield x
    if n2>=n1:
      if o1 not in ('+','-'):
        if not( o2=='-' and y2>n1):
          C= [(n2-n1,wrap(t2,False)+"-"+wrap(t1,o1 not in ('','*','/')),"-",n2,n1)]
          for x in expressions(C+B, processed):
            yield x
    

    # don't process x+(y-z), as (x+y)-z produces the same answer
    # don't process (x-z)+y, as (x+y)-z produces the same answer
    if o1!='-' and o2!='-':
      # don't process x+(y+z) if (x>z or x>y)
      if not( o2=='+' and (n1>x2 or n1>y2)):
        C=[(n1+n2,wrap(t1,False)+"+"+wrap(t2,False),"+",n1,n2)]
        for x in expressions(C+B, processed):
          yield x
#---------------------------------------------------------------------

# find all the solutions matching a target          
def allsolutions(A,target):
  for (x,t,o,a,b) in expressions(A):
    if x==target:
      print(x,"=",t)


def countallexpressions(A):
  count=0
  for (x,t,o,a,b) in expressions(A):
    count+=1
  return count  


# find how many targets in the range 101..999 are covered
def numtargets(A):
  results=set()
  for (x,t,o,a,b) in expressions(A):
    results.add(x)
  return len(results & set(range(101,1000)))

# find how many targets in the range 101..999 are covered
# and how many expressions cover those targest
def counttargets(A):
  results=set()
  count=0
  for (x,t,o,a,b) in expressions(A):
    if 101<=x<=999:
      results.add(x)
      count+=1
  return (count, len(results) )

# write expressions for all targets for a set of numbers A, until a gap above 1000 is found
def alltargets(A):

  filename = "Countdown numbers game coverage for "+ ",".join(str(i) for i in sorted(A)) +".txt"
  f=open(filename,'wb')
  lastx=-1
  for (x,t) in  sorted( (x,t) for (x,t,o,a,b) in expressions(A) ):
    if x>lastx:
      if x >1000 and x!=lastx+1:
        break
      f.write( (str(x) + "=" + t + "\n").encode('utf8') )
      lastx=x
  f.close()

if __name__=='__main__':
  from random import randint as RI
  
  print("The James Martin 952 game, https://www.youtube.com/watch?v=6mCgiaAFCu8")
  allsolutions([100,75,50,25,6,3], 952)
  
  print("The easiset game ever? https://www.youtube.com/watch?v=d3I2lafp9LY")
  allsolutions([1,4,8,9,10,50], 500) 

  print("These only have a few solutions each")
  allsolutions([50,25,1,7,10,10], 976) 
  allsolutions([100,75,1,1,3,5], 862) 
  allsolutions([50,75,2,5,5,6], 977) 
  allsolutions([100,50,10,10,7,1], 284) 
  allsolutions([75,25,1,4,6,10], 632) 
      
  print("Test random combinations of 2 top + 4 bottom")
  top2 = [ x for x in combinations([25,50,75,100],2)]
  bottom4 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),4)]
  print( "cards\ttargets\texpressions\texp/target")
  for _ in range(10):
    A= list(top2[RI(0,len(top2)-1)] + bottom4[RI(0,len(bottom4)-1)])
    c,n = counttargets(A)
    print(A,"\t", n ,"\t",c,"\t",round(c/n,1))          

  print("Test random combinations of 1 top + 5 bottom")
  bottom5 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),5)]
  print( "cards\ttargets\texpressions\texp/target")
  for _ in range(10):
    A=[RI(1,4)*25]+ list(bottom5[RI(0,len(bottom5)-1)])
    c,n = counttargets(A)
    print(A,"\t", n ,"\t",c,"\t",round(c/n,1))          

  print("Test random combinations of 2 top + 4 bottom - all expressions")
  top2 = [ x for x in combinations([25,50,75,100],2)]
  bottom4 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),4)]
  print( "cards\ttargets\texpressions\texp/target")
  for _ in range(10):
    A= list(top2[RI(0,len(top2)-1)] + bottom4[RI(0,len(bottom4)-1)])
    c = countallexpressions(A)
    print(A,"\t",c)          

  print("Test random combinations of 1 top + 5 bottom - all expressions")
  bottom5 = [ x for x in combinations(list(range(1,11))+list(range(1,11)),5)]
  print( "cards\ttargets\texpressions\texp/target")
  for _ in range(10):
    A=[RI(1,4)*25]+ list(bottom5[RI(0,len(bottom5)-1)])
    c = countallexpressions(A)
    print(A,"\t",c)          

  # these cover all targets 101..999
  alltargets([75,5,6,7,8,9])
  alltargets([25, 100, 4, 7, 10, 7])

  # these are useful for school game of noughts and crosses
  alltargets([2,3,4,5])
  alltargets([3,4,5,6])

  # [25, 100, 3, 8, 9, 6] covers all targets
  # [100, 75, 9, 4, 2, 5] covers all targets
  # [75, 25,6,7,8,9] covers all targets
  # [75,5,6,7,8,9] covers all targets
  # [100, 4, 7, 3, 1, 9] covers all targets
  # [100, 75,3,4,5,6] covers all targets
  # [25, 100, 4, 7, 10, 7] covers all targets
