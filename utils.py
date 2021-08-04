import math

def split(str):
    l=[]
    for s in str:
        l.append(s)
    return l

def arr(n,k):
    return math.comb(n,k)*math.factorial(k)

def append(l,a):
    l.append(a)
    s=set(l)
    l=list()
    for e in s:
        l.append(e)
    return l

def cass(s,l=list()):
    l.remove(s)
    return l

def list_contain(l,__object):
    for elt in l:
        if elt == __object:
            return [True,elt]
    return [False,None]
    