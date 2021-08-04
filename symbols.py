#---------In this module, we designed tools for buiding a symbols set like structure

from utils import arr,split
import random



class SetException(Exception):

    def __init__(self,msg) -> None:
        """Exception class raised relatively to the symbols base set"""

        super().__init__(self)
        self.msg=msg

    def __str__(self):
        return self.msg

class Superset:

    def __init__(self,s={}) -> None:
        """A built-in set like struture witch provide a way to store set as element """

        self.set=list()

    def add_set(self,s):
        if s not in self.set:
            self.set.append(s)

    def display(self):
        print(self.set)

    def contains(self,s):
        for elt in self.set:
            if elt == s:
                return True
        return False

class _Set:
    def __init__(self,sym=set()):
        """Initialyse the symbols set or alphabet's symbols, then storing them inside a python built-in immutable set"""
        try:
            self.symbols=sym

            if not self.is_atomic():
                raise SetException('Atomicity of symbols not verified: \n some symbols are formed using others')

        finally:
            self.card=len(self.symbols)

    def get_symbols(self):
        return self.symbols
    
    def contained(self,s):
        """Check if the given character belongs to the set"""

        if s in self.symbols:
            return True
        else:
            return False
    
    def to_list(self):
        l=list()
        for s in self.symbols:
            l.append(s)
        return l
    
    def is_atomic(self):
        """Checking the atomicity of each symbols contained in the set"""
        
        symbols=set()
        for e in self.symbols:
            if not e=='':
                symbols.add(e)

        for s in symbols:  #unicity first
            count=0
            for e in symbols:
                if s==e:
                    count+=1
            if count!=1:
                return False
            else:
                continue       
        temp=symbols.copy()
        for s in symbols:
            temp.remove(s)
            for e in temp:
                if s in e:
                    return False
                else:
                    continue
            temp=symbols.copy()

        return True
             
    def subset(self):
        trans=Superset()
        l=self.to_list()
        long=len(l)

        for elt in l:
            trans.add_set(set({elt}))
        
        for card in range(2,long+1):
            i=1
            while i<=arr(long,card):
                sub=set()
                j=1
                while j<=card:
                    while len(sub)<j and sub in trans.set:
                        pos=random.randrange(0,len(l))
                        sub.add(l[pos])
                    j+=1   
                trans.add_set(sub)
                print(sub)
                print('\n')
                i+=1
        trans.set.remove(set())
        trans.add_set({})
        return trans 
        


A=_Set({'a','b','c','d','e','f','g'})
partition = A.subset()
print("--------------------------------------------------------------")
partition.display()
print(len(partition.set))



class Word:

    def __init__(self,str='',alphabet=_Set()) -> None:
        """Class defining a 'word' readable by an Automate  object"""
        try:
            self.symbols=[None for i in range(0,len(str))]
            self.str=str
            self.chars=split(str)
            if not self.is_from_alphabet(alphabet):
                raise SetException("This Word object was not built using the provided alphabet...")
        finally:
            pass
    
    def __str__(self) -> str:
        return self.str

    def get_lenght(self):
        return len(self.symbols)

    def set_symbols_from(self,sigma=_Set())-> None:
        """Class procedure to split a word into elements of base alphabet sigma"""
        
        m=len(self.chars)
        
        _s=[]
        symbols=set()
        for e in sigma.symbols:
            "ignoring the empty word"
            if not e == '':
                symbols.add(e)
    
        for s in symbols:
            _s=split(s)
            n=len(s)
            for i in range(0,m-n+1):
                if _s==self.chars[i:i+n]:
                    self.symbols[i]=s
                i=+1

        """Eliminating None values from the list object self.symbols"""
        temp=[]
        for elt in self.symbols:
            if elt==None:
                pass
            else:
                temp.append(elt)
        self.symbols=temp
                
            
    
    def is_from_alphabet(self,sigma=_Set()):
        
        self.set_symbols_from(sigma)
        
        if len("".join(self.symbols)) < len(self.str):
        
            return False
        
        return True

