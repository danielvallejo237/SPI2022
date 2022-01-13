import botutils
import intutils


def Ask(string):
    final=""
    l1=botutils.processTweet(string)
    l2=[] #Recuperador Zeltzyn y Darío
    l3=[]
    final=botutils.Interact(l1,l2,l3)
    print(final)
    return final

def ClasificadorInt(string):
    return intutils.IntEspecificas(string)

if __name__=="__main__":
    pass