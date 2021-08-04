from data_structure import Stacks

class retype():
    CHAR=0
    UNION=1
    CONCAT=2
    ITER=3
    BRACKET=4

class ReNode:

    def __init__(self,str='') -> None:
        self.str=str
        self.prior=self.set_type(self)

    @staticmethod 
    def set_type(self):
        prior=0
        if self.str == '+':
            prior=retype.UNION
        elif self.str == '.':
            prior= retype.CONCAT
        elif self.str == '*':
            prior = retype.ITER
        elif self.str=='(' or self.str==')':
            prior = retype.BRACKET
        else:
            prior = retype.CHAR
        return prior

class Pattern():
    def __init__(self,string='') -> None:
        self.str=string
        self.splited=[]
        self.postfix=[]
        self.split()
        self.postfixed()

    def split(self):
        for e in self.str:
            self.splited.append(ReNode(e))

    
    def postfixed(self):
        op_pile=Stacks()
        
        for re in self.splited:
            if re.prior == retype.CHAR:
                self.postfix.append(re)
            elif re.prior != retype.BRACKET:
                if op_pile.is_empty():
                    op_pile.push(re)
                else:
                    while op_pile.get_heap().prior > re.prior:
                        if op_pile.get_heap().prior != retype.BRACKET:
                            self.postfix.append(op_pile.pop())
                            if op_pile.is_empty():
                                break
                        else:
                            break
                    op_pile.push(re)
            else:
                if re.str == "(":
                    op_pile.push(re)
                elif re.str == ")":
                    while op_pile.get_heap().str != "(":
                        self.postfix.append(op_pile.pop())
                    op_pile.pop()

        while len(op_pile) != 0:
            self.postfix.append(op_pile.pop())
    
    def post_str(self):
        _str=[]

        for elt in self.postfix:
            _str.append(elt.str)
        
        return _str


    
    
                                            
        
    
