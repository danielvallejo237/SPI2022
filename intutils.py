'''
@Author danielvallejo237
'''

import fasttext
import fasttext.util
import numpy as np
from scipy.spatial import distance
import re
import unidecode

ft = fasttext.load_model('/home/danielvaal/fastText/cc.es.100.bin')

def return_significant_vector(string,FastText=ft):
    splitted=string.split()
    sigs=np.zeros(100)
    for s in splitted:
        sigs=sigs+FastText.get_word_vector(s)
    sigs=sigs/len(splitted)
    return sigs

def cossine_distance(v1,v2):
    return distance.cosine(v1,v2)

def similaridad_frase(s1,s2,FT=ft):
    v1=return_significant_vector(s1,FastText=FT)
    v2=return_significant_vector(s2,FastText=FT)
    return cossine_distance(v1,v2),distance.euclidean(v1,v2)

saludos=["buenas tardes","buenos dias","hola","buenas noches","hola que tal","hola buenas tardes","Hola Garambubot"]
despedidas=["adios","hasta luego","hasta pronto","nos vemos","chao","bye"]

def IntGen(frase,greet,desp,fst=ft):
    gscores=[]
    efscr=[]
    for g in greet:
        a,b=similaridad_frase(frase,g,FT=fst)
        gscores.append(a)
        efscr.append(b)
    mg=min(gscores)
    dg=min(efscr)
    dscores=[]
    defscr=[]
    for g in desp:
        a,b=similaridad_frase(frase,g,FT=fst)
        dscores.append(a)
        defscr.append(b)
    md=min(dscores)
    dmd=min(defscr)
    gs=[mg,md]
    gs1=[dg,dmd]
    if min(gs)<0.4:
        if 1+gs.index(min(gs)) == 1+gs1.index(min(gs1)):
            return 1+gs.index(min(gs))
        else: 
            return 3
    else:
        return 3 

def hasHashTag(string):
    return len(re.findall(r"#[\w]+",string))>0

def IntEspecificas(frase,greet=saludos,desp=despedidas,fst=ft):
    frase=unidecode.unidecode(frase)
    intencion=IntGen(frase,greet,desp,fst)
    if intencion==3:
        if hasHashTag(frase):
            intencion=4
    if hasHashTag(frase):
        intencion=4
    return intencion

if __name__=="__main__":
    pass