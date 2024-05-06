import pandas as pd 
import numpy as np 
from datetime import datetime as dt 

df = pd.read_csv('[REDACTED FILE PATH]',
dtype = {'Call Number': str, 
'Received DtTm': object,
'Dispatch DtTm': object,
'On Scene DtTm': object,
'Transport DtTm': object,
'Hospital DtTm': object,
'Battalion': object,
'Station Area':object,
'Box': object})

#print(df.dtypes)

#Call Number,Unit ID,Incident Number,
#Call Date,Watch Date,Received DtTm,
#Entry DtTm,Dispatch DtTm,Response DtTm,
#On Scene DtTm,Transport DtTm,Hospital DtTm,
#Call Final Disposition,Available DtTm,Address,
#City,Zipcode of Incident,Battalion,
#Station Area,Box,Original Priority,
#Priority,Final Priority,ALS Unit,
#Call Type Group,Number of Alarms,Unit Type,
#Unit sequence in call dispatch,Fire Prevention District,Supervisor District,
#Neighborhooods - Analysis Boundaries,RowID

date_format = "%m/%d/%Y %I:%M:%S %p"

#Formating columns 
try: 
    df['Call Date']= pd.to_datetime(df['Call Date'])
    df['Received DtTm'] = pd.to_datetime(df['Received DtTm'] , format = date_format)
    df['Response DtTm'] = pd.to_datetime(df['Response DtTm'], format = date_format )
    df['On Scene DtTm'] = pd.to_datetime(df['On Scene DtTm'],format = date_format)
    df['Transport DtTm'] = pd.to_datetime(df['Transport DtTm'], format = date_format)
    df['Hospital DtTm'] = pd.to_datetime(df['Hospital DtTm'], format = date_format)

    #print(df['Call Date'].head())

except Exception as error:
    print('An error occurred:', error)

df.to_csv('Clean_Fire_Department_Calls.csv', sep=',', index=False, encoding='utf-8')





