import pandas as pd
import numpy as np
from datetime import datetime, timedelta  
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

### Q.4: Which battalion responds to the most calls? ### 
sns.countplot(
    data = df.sort_values(by ='Battalion'),
    x = 'Battalion',
    hue = 'Battalion'
)
plt.title('Countplot of Battalion Calls')
plt.ylabel('Count')
plt.show()

#Q.5: What is the most common call type? ###
sns.countplot(
    data = df,
    x = 'Call Type Group',
    hue = 'Call Type Group',
    legend = False
    
)
plt.title('Countplot of Call Types')
plt.ylabel('Count')
plt.show()

#Q.6: How often does the unit include ALS resources? ### 
sns.countplot(
    data = df,
    x = 'ALS Unit',
    hue = 'ALS Unit',
    stat = 'percent',
    legend = False 
)
plt.title('Percentage Inclusion of ALS Unit')
plt.ylabel('Percent')
plt.show()

