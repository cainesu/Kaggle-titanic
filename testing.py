# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualization 


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

df= pd.read_csv("/Users/CaineSu/Desktop/kaggle/input/aug_train.csv")
print(df['experience'].head(10))
df.shape
df.info()
pd.set_option('max_columns', None)
df['gender'].loc[df['gender'].isnull()==True]='Undefined' #since nan values is really high we will treat it as a seperate category
df.gender.value_counts()
df.gender.isna().sum()

df.experience.replace('>20','22',inplace=True) # replacing special chars(like >,+) with numbers
df.experience.replace('<1','0',inplace=True)
df.experience=pd.to_numeric(df.experience)
df['experience']=np.where(df['experience']>10,'Senior-level', np.where(df['experience']>3,'Intermediate-level' ,'Entry-Level'))
# here we are creating a class interval for each level of experience
df['experience'].value_counts().sum()
print(df.head(10))
print(df['experience'].head(10))
print(df.isnull().sum())
