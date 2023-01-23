import os
import pandas as pd
import pickle

### read all csv
dicts=pickle.load(open('../dataset_path.pkl','rb'))## a file that stores dataset path, can be generated by get_dict.py
groups=dicts.keys()


### combine all samples
df_score=pd.DataFrame(columns=['rs429358','rs7412'])
df_geno=pd.DataFrame(columns=['ref1','alt1','rs429358','ref2','alt2','rs7412'])

for k in groups:
    df_s=pd.read_csv('../sample_score/'+k+'_0000001655-interval.csv',index_col=0)
    df_g=pd.read_csv('../sample_geno/'+k+'_0000001655-interval.csv',index_col=0)
    df_score=pd.concat([df_score,df_s])
    df_geno=pd.concat([df_geno,df_g])


### get APOE based on genotype
## rs429358 C->C & rs7412 T->C
## which means that rs429358: 1/1 --> score: 2 & rs7412: 0/* --> score: 0,1
apoe_prop=sum(df_score[df_score['rs429358']!=0]['rs7412']<2)/df_score.shape[0]#calculate apoe proportion
apoe_prop

### save whether a patient is apoe4 mutated
is_apoe=df_score[df_score['rs429358']!=0]['rs7412']<2
is_apoe.index.astype(str)
is_apoe.to_csv('../apoe_ids.csv')

