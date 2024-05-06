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

### Q.1: What is the distribution of calls across the years recorded? ###

#Pull receive datetime 
df1= pd.DataFrame()
df1['received'] = pd.to_datetime(df['Received DtTm']).dt.date 

df1['received'] = pd.to_datetime(df1['received'])

#Separate year and month 
df1['year'] = df1['received'].dt.year
df1['month'] = df1['received'].dt.month


try: 
    df2 = df1.groupby(['year','month']).size().reset_index(name = 'count')
except Exception as error: 
    print('erorr:', error)


#Pivot dataframe to wide-form representation 
try: 
    df2_wide = df2.pivot(index='month', columns='year',values='count')
except Exception as error:
    print('error:',error)

#Plot lineplot 
try: 
    ax = sns.lineplot(
        data = df2_wide
    )

    sns.move_legend(ax , 'upper left', bbox_to_anchor = (1,1))

    plt.title('Monthly Lineplot of Fire Incidents in San Francisco')
    plt.ylabel('Count')
    plt.xlabel('Month')
    plt.show()
except Exception as error: 
    print('error:',error)