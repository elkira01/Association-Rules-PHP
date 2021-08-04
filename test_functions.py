from components import *
from data_structure import *
from langage import *
from symbols import *
from utils import *

def build_automate(type,alphabet):
    
    if type=='1':
        Dfa=Automate(alphabet)
        nb_node=0

        print("Combien etats comporte l'automate??\n")
        nb_node=input()
        print("Combien de Transitions non terminales seront ajoutees ?? \n")

        t=[]
        print("Entrer les etiquettes des etats, sous forme d'entiers\n\n")
        for i in range(0,int(nb_node)):
            t.append(State(int(input())))
        Dfa.add_states_from(t)

        for elt in Dfa.states:
            print("\n\nEntrer les transitions d'origine "+str(elt.label)+" sans omettre une potentielle transition finale :")
            print("\nNombre de transitions :")
            nb=input()
            for i in range(0,int(nb)):
                print("\nDestination : (entrer '.' si finale)")
                d=input()
                print("\nEtiquette : (entrer '.' si finale)")
                e=input()
                if d=='.':
                    Dfa.add_trans(elt)
                else:
                    Dfa.add_trans(elt,Dfa.get_state(int(d)),{e})
        print("\nEtat initial :")
        init=input()
        Dfa.set_start(Dfa.get_state(int(init)))
        Dfa.set_finals()

        return Dfa

def build_epsilon(alphabet):
    

    Dfa=eNDFA(alphabet)
    nb_node=0

    print("\nCombien etats comporte l'automate??\n")
    nb_node=input()
    print("Combien de Transitions non terminales seront ajoutees ?? \n")

    t=[]
    print("Entrer les etiquettes des etats, sous forme d'entiers\n\n")
    for i in range(0,int(nb_node)):
        t.append(State(int(input())))
    Dfa.add_states_from(t)

    for elt in Dfa.states:
        print("\n\nEntrer les transitions d'origine "+str(elt.label)+" sans omettre une potentielle transition finale :")
        print("\nNombre de transitions :")
        nb=input()
        for i in range(0,int(nb)):
            print("\nDestination : (entrer '.' si finale)")
            d=input()
            print("\nEtiquette  :(Entrer '.' si mot vide ou finale)")
            e=input()
            if e=='.':
                if d == '.':
                    Dfa.add_trans(elt)
                else:
                    Dfa.add_trans(elt,Dfa.get_state(int(d)),{''})
            else:
                Dfa.add_trans(elt,Dfa.get_state(int(d)),{e})
    print("\nEtat initial :")
    init=input()
    Dfa.set_start(Dfa.get_state(int(init)))
    Dfa.set_finals()

    return Dfa


