import botutils
import intutils
import sbotutils

def Ask(string,doublecheck=False):
    final=""
    l1=botutils.processTweet(string)
    l2=[] #Recuperador Zeltzyn y Darío
    l3=[]
    if doublecheck:
        l2=sbotutils.processTweet2(string)
    final=botutils.Interact(l1,l2,l3)
    #print(final)
    return final

def ClasificadorInt(string):
    return intutils.IntEspecificas(string)

if __name__=="__main__":
    pass