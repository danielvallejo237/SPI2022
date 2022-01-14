import os as os
import numpy as np
import pandas as pd
import re
import botutils

zx=pd.read_csv('./recipies_full_v2.csv',index_col=0)

def Recuperador(ingredientes,df=zx,Criterio='Ingredientes'):
    len_ing=[]
    match=[]
    qw=0
    for i in range(len(df)):
        len_ing.append(len(df.Ingredientes.iloc[i].split(',')))

    df['Num_I']=len_ing

    for j in range(len(df)):
        for k in range(len(ingredientes)):
            if ingredientes[k] in df[Criterio].iloc[j]:
                qw+=1
        match.append(qw)
        qw=0
    df['Match']=match
    df['Dif']=df['Num_I']-df['Match']
    df['Score']=df['Match']- 0.3*df['Dif']
    df=df.sort_values('Score')
    idxs=df.index[-3:].to_list() 
    idxs=[str(i) for i in idxs]
    return idxs

def processTweet2(tweet,df=zx):
    KWD=re.findall('#[\w]+',tweet)
    KWD=[k[1:] for k in KWD]
    KWD=botutils.lematize(KWD)
    return Recuperador(KWD,df)


if __name__=="__main__":
    pass