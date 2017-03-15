import pandas as pd

file="input/products.csv"
file="output/attributes.csv"

simpleDF=pd.DataFrame()

def createSimple(row):
	pass


def createChilds(df):
	df.apply(lambda x: createSimple(x),axis=1)


df=pd.read_csv(file)
attr=""
attributes=["flags", "banner","flagpoles","apparel","bracelet","stands","case","others"]
for attr in attributes:
	createChilds(df[df.attributes==attr])