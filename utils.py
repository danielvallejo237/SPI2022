'''
@Author danielvallejo237
'''

import unidecode
import json
import re
import numpy as np
import regex

class RecetaVS:
    def __init__(self,texto):
        self.texto=texto
        self.author=""
        self.ing=[]
        self.titulo=""
        self.preparacion=""
        self.unaccented=unidecode.unidecode(self.texto.lower())
        self.resumen=""
        self.source=""
        if self.isRecipie():
            self.gettitle()
            self.get_recipie()
            self.get_ingredients()
            self.resumen=self.getKwd()
    def isRecipie(self):
        "Vemos si un texto es una receta con base en las palabras que contiene"
        score=0.0
        scores={}
        scores['elaboracion']=0.3
        scores['nthoki']=0.5
        scores['ingredientes']=0.1
        score+=len(re.findall(r'elaboracion:',self.unaccented))*scores['elaboracion']
        score+=len(re.findall(r'nthoki',self.unaccented))*scores['nthoki']
        score+=len(re.findall(r'ingredientes:',self.unaccented))*scores['ingredientes']
        self.hasIng=len(re.findall(r'ingredientes:',self.unaccented))*scores['ingredientes']>0
        if score>0.5:
            return True 
        else:
            return False
    def gettitle(self):
        split=self.texto.split("\n")
        if split[0] !="":
            self.titulo=split[0]
        else:
            self.titulo=split[1]
        self.author=split[2]
        self.titulo=unidecode.unidecode(self.titulo.lower())
        self.author=unidecode.unidecode(self.author.lower())
    def get_recipie(self):
        rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('elaboracion', 'nthoki'))
        self.preparacion=rgx.findall(self.unaccented)[0][0]
        self.preparacion=' '.join(self.preparacion.split('\n'))
    def get_ingredients(self):
        if self.hasIng:
            rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('ingredientes', 'elaboracion'))
            ingredientes=rgx.findall(self.unaccented)[0][0]
            splt=ingredientes.split('\n')
            splt=splt[1:-1]
            self.ing=splt
    def getKwd(self):
        nstr=""
        if len(self.ing)>0:
            for s in self.ing:
                nstr=nstr+' '.join(re.findall(r'[^\d\W]+',s))+' '
        return unidecode.unidecode(nstr.lower())
    
    def add_source(self,source):
        self.source=source
        
    def toJSON(self):
        kw=self.getKwd()
        data_set = {"name": self.titulo, "author": self.author, "ing": self.ing, "prep":self.preparacion, "kwd":kw,"source":self.source}
        json_dump = json.dumps(data_set)
        return json_dump


class RecetaGeneral:
    def __init__(self,texto):
        self.texto=texto
        self.author=""
        self.ing=[]
        self.titulo=""
        self.preparacion=""
        self.unaccented=unidecode.unidecode(self.texto.lower())+'<pageend>'
        self.resumen=""
        self.source=""
        if self.isRecipie():
            self.gettitle()
            self.get_recipie()
            self.get_ingredients()
            self.resumen=self.getKwd()
    def isRecipie(self):
        "Vemos si un texto es una receta con base en las palabras que contiene"
        score=0.0
        scores={}
        scores['elaboracion']=0.3
        scores['preparacion']=0.3
        scores['ingredientes']=0.5
        score+=len(re.findall(r'elaboracion:',self.unaccented))*scores['elaboracion']
        score+=len(re.findall(r'preparacion:',self.unaccented))*scores['preparacion']
        score+=len(re.findall(r'ingredientes:',self.unaccented))*scores['ingredientes']
        self.hasIng=len(re.findall(r'ingredientes:',self.unaccented))*scores['ingredientes']>0
        if score>0.5:
            return True 
        else:
            return False
    def gettitle(self):
        split=self.texto.split("\n")
        indice=1
        if split[0] !="":
            self.titulo=split[0]
        else:
            self.titulo=split[0]+split[1]
            indice+=1
        while(len(re.findall('\w+',self.titulo)[0])<3):
            #print(re.findall('\w+',self.titulo)[0])
            self.titulo=re.findall('\w+',self.titulo)[0] + split[indice]
            indice+=1
        if len(re.findall(r'dientes',split[indice].lower()))>0:
            self.author=""
        else:
            self.author=split[indice]
        self.titulo=unidecode.unidecode(self.titulo.lower())
        self.author=unidecode.unidecode(self.author.lower())
    def get_recipie(self):
        try:
            rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('elaboracion', '<pageend>'))
            self.preparacion=rgx.findall(self.unaccented)[0][0]
        except:
            rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('preparacion', '<pageend>'))
            self.preparacion=rgx.findall(self.unaccented)[0][0]
        self.preparacion=' '.join(self.preparacion.split('\n'))
    def get_ingredients(self):
        if self.hasIng:
            try:
                rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('ingredientes', 'elaboracion'))
                ingredientes=rgx.findall(self.unaccented)[0][0]
            except:
                rgx = regex.compile(r'(?si)(?|{0}(.*?){1}|{1}(.*?){0})'.format('ingredientes', 'preparacion'))
                ingredientes=rgx.findall(self.unaccented)[0][0]
            splt=ingredientes.split('\n')
            splt=splt[1:-1]
            self.ing=splt
    def getKwd(self):
        nstr=""
        if len(self.ing)>0:
            for s in self.ing:
                nstr=nstr+' '.join(re.findall(r'[^\d\W]+',s))+' '
        return unidecode.unidecode(nstr.lower())
    
    def add_source(self,source):
        self.source=source
        
    def toJSON(self):
        kw=self.getKwd()
        data_set = {"name": self.titulo, "author": self.author, "ing": self.ing, "prep":self.preparacion, "kwd":kw,"source":self.source}
        json_dump = json.dumps(data_set)
        return json_dump