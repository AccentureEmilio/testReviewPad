'''
Created on 17 ott 2024

@author: emilio.giliberti
'''
import pandas as pd
from fileinput import input
from pip._vendor.distlib.compat import raw_input
import numpy as np
import warnings

#metodo che confronta le colonne dei due file
def elaborateFiles(df2, date, column_name_from_ifactory):
    column_name_from_rto_temp = df2[date].replace('\xa0', np.nan, regex=True)
    coulmn_name_from_rto = column_name_from_rto_temp.dropna()
    # Confronta le colonne
    #uguaglianze = colonna_nomi.isin(colonna_nomi2)
    inIfactoryNotInRTO = ~column_name_from_ifactory.isin(coulmn_name_from_rto)
    inRTONotInIfactory = ~coulmn_name_from_rto.isin(column_name_from_ifactory)
    print('\n **** CHECK RELATIVI AL GIORNO: ' + date + ' ***\n')
    print("\nValori in IFACTORY non presenti in RTO:")
    if column_name_from_ifactory[inIfactoryNotInRTO].empty:
        print("Tutti i nominativi presenti su ifactory sono presenti su RTO")
    else:
        print(column_name_from_ifactory[inIfactoryNotInRTO])
    print("\nValori su RTO non presenti in ifactory:")
    if coulmn_name_from_rto[inRTONotInIfactory].empty:
        print("Tutti i nominativi presenti su RTO sono presenti su ifactory")
    else:
        print(coulmn_name_from_rto[inRTONotInIfactory])


#metodo che prepara i file
def prepareFiles(pd):
    

    file1_path = "ifactory_25_11.xlsx"
    file2_path = "RTO_plan_modificato_25_11.xlsx"
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)
    area = 'eCommerce Digital Area' # Area filtrata
    unique_date_from_file = 'Location Request Date' #prendo univocamente le date dall'estrazione
    unique_date = df1[unique_date_from_file].unique()
    list_date = sorted(unique_date.tolist())
    return list_date, df1, area, df2

# Disabilita i FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None) 

range1_str = raw_input("Inserisci il range dei posti minimo: ")
range2_str = raw_input("Inserisci il range dei posti massimo: ")

range1 = int(range1_str)
range2 = int(range2_str)

list_date, df1, area, df2 = prepareFiles(pd)

print(df2.columns)
for date in list_date:
    #column_name_from_ifactory = df1[(df1['Location Request Date'] == date) & (df1['Project'] == area) ''& (df1['Choosed Seat'] >= range1) & (df1['Choosed Seat'] <= range2)]['Employee']
    column_name_from_ifactory = df1[(df1['Location Request Date'] == date) & (df1['Project'] == area)]['Employee']
    if date not in df2.columns:
        print(f"La data '{date}' non è presente nel file RTO.")
        continue
    else:
        elaborateFiles(df2, date, column_name_from_ifactory)
input("premi un tasto per chiudere...")

