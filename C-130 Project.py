import pandas as pd
import csv

df = pd.read_csv('C:/Users/admin/C-130 Project/total_stars.csv')
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
final = df.dropna()
final.reset_index(drop=True,inplace = True)
final.to_csv('final.csv')