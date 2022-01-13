import json
import numpy as np
import re
import stanza
from spacy_stanza import StanzaLanguage
import unidecode
import random


NLPProc=None
JSONOBJ=None
with open("recipes_full_v2.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        JSONOBJ=jsonObject
        jsonFile.close()
snlp = stanza.Pipeline(lang="es")
NLPProc = StanzaLanguage(snlp)

def lematize(words,lematizer=NLPProc):
    lematizadas=[unidecode.unidecode(lematizer(p)[0].lemma_).lower() for p in words]
    return lematizadas
def query_score(palabras,text,title):
    st=""
    for p in palabras:
        st=st+p+"|"
    st=st[:-1]
    rx=re.compile(st)
    return 10*len(re.findall(rx,''.join(title.split())))+len(re.findall(rx, ''.join(text.split())))

def query(palabras,Json=JSONOBJ,lematizer=NLPProc):
    scores={}
    palabras=lematize(palabras,lematizer=lematizer)
    for i,j in enumerate(Json):
        js=json.loads(Json[j])
        scores[j]=query_score(palabras,js['kwd'],js['name'])
    sort_orders = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top3=sort_orders[:3]
    lst=[]
    if top3[0][1] > 0:
        lst.append(top3[0][0])
    if top3[1][1] > 0:
        lst.append(top3[1][0])
    if top3[2][1] > 0:
        lst.append(top3[2][0])
    return lst

def processTweet(tweet,Json=JSONOBJ,lematizer=NLPProc):
    KWD=re.findall('#[\w]+',tweet)
    KWD=[k[1:] for k in KWD]
    return query(KWD,Json,lematizer)

def Interact(l1,l2,l3,Json=JSONOBJ):
    L=l1+l2+l3
    L=list(set(L))
    random.shuffle(L)
    L=L[:min(3,len(L))]
    result=""
    if len(L)>0:
        for l in L:
            js=json.loads(Json[l])
            result=result+' Nombre: '+js['name']+' No.Ingredientes: '+str(len(js['ing']))+" Link: "+js['source']+' \n'
    return result

if __name__=="__main__":
    pass
