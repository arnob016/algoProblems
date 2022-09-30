from math import *


l2=[]
n= int(input())
l1 = input().split()
print(l1)
for x in l1:
    l2.append(int(x))

l2.sort()
print(l2)
if n%2!=0:
    halv = int(n/2)
    print(l2[halv])
elif n%2==0:
    h = l2[n/2]
    l = l2[n/2+1]
    print((h+l)/2)
# simplify the solution and solve the problem with even numbers
