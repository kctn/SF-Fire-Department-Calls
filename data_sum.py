import pandas as pd 
import numpy as np 

df = pd.read_csv('/Users/kaceyton/Documents/IBM DA/fire incidents SF/Fire_Department_Calls_For_Service__2016__20240124.csv')

#print(df.head())

print(df.size)

#Call Number,Unit ID,Incident Number,
#Call Date,Watch Date,Received DtTm,
#Entry DtTm,Dispatch DtTm,Response DtTm,
#On Scene DtTm,Transport DtTm,Hospital DtTm,
#Call Final Disposition,Available DtTm,Address,
#City,Zipcode of Incident,Battalion,
#Station Area,Box,Original Priority,
#Priority,Final Priority,ALS Unit,
#Call Type Group,Number of Alarms,Unit Type,
#Unit sequence in call dispatch,Fire Prevention