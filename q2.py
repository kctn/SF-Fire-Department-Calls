import pandas as pd
import numpy as np
from datetime import datetime as dt 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('Clean_Fire_Department_Calls.csv',
dtype = {'Call Number': str, 
'Received DtTm': object,
'Dispatch DtTm': object,
'On Scene DtTm': object,
'Transport DtTm': object,
'Hospital DtTm': object,
'Battalion': object,
'Station Area':object,
'Box': object})

### Q.2: When do most of the calls occur during the year? Time of day? 

#Pull receive datetime 
df_received = pd.DataFrame()
df_received['Received']= pd.to_datetime(df['Received DtTm'])
#dtype:  Received    datetime64[ns]

#Extract hour 
df_received['Hour']=df_received['Received'].dt.hour 
df_received['Hour'].astype(int)
#Time: object

#Plot countplot 
try: 
    sns.countplot(data = df_received,
    x='Hour',
    hue = 'Hour',
    legend = False 
    )
    plt.title('Countplot of Fire Incidents in SF by Hour of Day')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Count')
   
    plt.show()
except Exception as error: 
    print('Error:', error)

