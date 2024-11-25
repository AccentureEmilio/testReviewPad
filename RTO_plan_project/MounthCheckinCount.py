'''
Created on 24 ott 2024

@author: emilio.giliberti
'''

import pandas as pd
from fileinput import input
from datetime import datetime

from pip._vendor.distlib.compat import raw_input
import numpy as np
import warnings
import webbrowser

# Disabilita i FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

'''conte le presenze in ufficio'''
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None) 

file1_path = "ifactory_sett.xlsx"
file2_path = "risorse.xlsx


df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)


area = 'eCommerce Digital Area'  # Area filtrata
unique_date_from_file = 'Location Request Date'
status='checkin'


column_in_risorse= df2['ListaConfronto']
column_name_from_ifactory = df1[(df1['Project'] == area)  & (df1['Status'] == status)]['Employee'].value_counts();

conteggio_finale = {}

# Verificare ogni dato se è presente nel file di confronto
for dato in column_name_from_ifactory.index:
    if dato in df2['ListaConfronto'].values:
        conteggio_finale[dato] = column_name_from_ifactory[dato]

# Stampare i risultati
for dato, conteggio in conteggio_finale.items():
    print(f"{dato}: {conteggio} presenze")