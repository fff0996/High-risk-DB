import os
import pandas as pd 
import scipy as sp
import csv
import sys
import numpy as np
import subprocess




disease = sys.argv[1]
#case = sys.argv[2]
#result = sys.argv[3]


#case = pd.read_csv(case,sep="\t",index_col=False)

with open(disease) as f:
    ICD10 = f.read().splitlines()
dic ={}
for d in(ICD10):
    i = d[0]
    path = "/BiO/Hyein/90Traits/BT/ICD10/"
    path = path+i+"/"+d+"/case.txt"
    
    case = pd.read_csv(path,sep="\t",index_col=False)
    value = case["FID"].values.tolist()
    dic[d] = value


result = pd.DataFrame.from_dict(dic,orient='index',dtype=None)
result = result.replace(np.nan,-9,regex=True)
result = result.astype('int')
#print(result)
#print(result.dtypes)
#value = case["FID"].values.tolist()
#string = ','.join(str(x) for x in value)
#dic = {disease:string}
#print(dic)

#if(os.stat(result).st_size ==0):
#    result = pd.DataFrame()

#dic = {disease:value}

#result = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dic.items()]))

#print(result)
#elif(len(value) ==0):
    
#    empty = ["",""]
#    result = pd.read_csv(result,sep="\t",index_col=False)
#    result[disease] = empty
#else:
#    result = pd.read_csv(result,sep="\t",index_col=False)
#    result[disease] = value
#result = pd.DataFrame({disease:value})
#print(result)
result.to_csv("result.txt",sep="\t",index=True)

