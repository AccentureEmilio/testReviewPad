'''
Created on 17 ott 2024

@author: emilio.giliberti
'''
import pandas as pd
from fileinput import input
from pip._vendor.distlib.compat import raw_input
import numpy as np
import warnings

# Disabilita i FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None) 

range1_str = 3001
range2_str = 3010

file1_path = "ifactory.xlsx"
file2_path = "RTO_plan.xlsx"


#da file rto eliminare riga 1 e 3, modificare 2

df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)


righe_da_eliminare = [1,3]
df2 = df2.drop(righe_da_eliminare)
df2.to_excel('file_modificato.xlsx', index=False)

area = 'eCommerce Digital Area'  # Area filtrata
unique_date_from_file = 'Location Request Date' #prendo univocamente le date dall'estrazione
unique_date = df1[unique_date_from_file].unique()
list_date=sorted(unique_date.tolist())

   
