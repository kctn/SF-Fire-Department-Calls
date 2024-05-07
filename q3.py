import pandas as pd
import numpy as np
from datetime import datetime, timedelta  
import seaborn as sns 
import matplotlib.pyplot as plt

#Convert csv to df 
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

### Q.3: What is the average time interval between different en routes of call times? ### 

#Create df with desired columns 
#Pull receive , on_scene columns 
df_e = pd.DataFrame()
df_e['receive']= (df['Received DtTm'])
df_e['on_scene']= (df['On Scene DtTm'])

#Pull response columns 
df_e['response']= (df['Response DtTm'])

#Pull transport, hospital columns 
df_e['transport']= (df['Transport DtTm'])
df_e['hospital']= (df['Hospital DtTm'])



#Create holding df 
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()

#Convert timedelta to minutes
def tomin(x):
    return ((x) / timedelta(minutes=1))

#Absolute value minutes
def rounder(x):
    return round((x)).abs()

#Put time deltas into dataframes
try:
    df1['td_rr']= (df_e['response'].apply(pd.Timestamp) - df_e['receive'].apply(pd.Timestamp))
    df2['td_or']= (df_e['on_scene'].apply(pd.Timestamp) - df_e['receive'].apply(pd.Timestamp))
    df3['td_ht']= (df_e['hospital'].apply(pd.Timestamp) - df_e['transport'].apply(pd.Timestamp))
   
except Exception as error: 
    print("Error:", error)

#Remove NaN vallues 
try: 
    df1 = df1.dropna().reset_index()
    df2 = df2.dropna().reset_index()
    df3 = df3.dropna().reset_index()

    df1 = df1.drop(columns = ['index'])
    df2 = df2.drop(columns = ['index'])
    df3 = df3.drop(columns = ['index'])

except Exception as error: 
    print("Error:", error)

#Combine df for all time deltas
try:
    cdf = df1.join([df2,df3])
    #print(cdf.head())
except Exception as error:
    print("Error:", erorr)
    #print(cdf.head(10))

#Convert to int minutes
try: 
    cdf[['td_rr','td_or','td_ht']]= cdf[['td_rr','td_or','td_ht']].apply(tomin)
    cdf[['td_rr','td_or','td_ht']]= cdf[['td_rr','td_or','td_ht']].apply(rounder)
    #print(cdf.head())
except Exception as error: 
    print("Error:", error)


try:
    sns.boxplot(
        data = cdf,
        showfliers = False,
        legend = 'full' 
    )

    plt.ylabel('Time Elapsed (min)')
    plt.xlabel('Transportation Route')
    plt.title('Distribution of Elapsed Call Times')
    plt.legend(title = 'Transport Type', labels = ['Response/Receive','On Scene/Response','Hospital/Transport'])

    plt.show()

except Exception as error: 
    print("Error:", error)



