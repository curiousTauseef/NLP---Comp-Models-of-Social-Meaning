"""
Tejas Dharamsi td2520: 
Data Assignment 1 
"""


import pandas as pd
import numpy as np

dataset = pd.read_csv('imdb-adjcoord.csv')
#Load the dataset
dataset = dataset.fillna(0)
dataset.Adj1Pol.replace(to_replace=dict(POS=1, NEG=0), inplace=True)
dataset.Adj2Pol.replace(to_replace=dict(POS=1, NEG=0), inplace=True)
"""
for i in range(len(dataset)):
	print(i)
	if(d1.loc[i,'Adj1Pol']=="POS"):
		d1.loc[i,'Adj1POL']=1
	if(d1.loc[i,'Adj1Pol']=="NEG"):
		d1.loc[i,'Adj1POL']=0"""
#print(dataset.loc[['Adj1Pol',])
#print(dataset)

d1=dataset[['PolMatch','Adj1Pol','Adj2Pol','Coord']]
d1['Values']=d1.Adj1Pol^d1.Adj2Pol
d2= d1.loc[:,['PolMatch','Coord','Values']]

print("For Coord OR:")
print("Total")
print(d2[d2.Coord == "or"].count())
d3= d2.loc[d2.Coord == "or"]
print("Contrasting : ")
print(d3.loc[d3.Values == 1].count())
print("Matching : ")
print(d3[d3.PolMatch == 1].count())

print("")
print("For Coord Versus :")
print(d2[d2.Coord == "versus"].count())
d3= d2.loc[d2.Coord == "versus"]
print(d3.loc[d3.Values == 1].count())
print(d3[d3.PolMatch == 1].count())

print("")
print("For Coord Nor :")
print(d2[d2.Coord == "nor"].count())
d3= d2.loc[d2.Coord == "nor"]
print(d3.loc[d3.Values == 1].count())
print(d3[d3.PolMatch == 1].count())


