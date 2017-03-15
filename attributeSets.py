import pandas as pd
import re

attrList = []

def attr(row):
	lname=row["name"].lower()
	if re.match(r'.*\b(case|coin|box)(\b|s\b).*',lname):
		attrList.append("case")
	elif re.match(r'.*\b(bunting|plate|fan|strap|storm|signal|ensign|bracket|ornament|halyard|medallion)(\b|s\b).*',lname):
		attrList.append("others")		
	elif re.match(r'.*(shirt|hoodie|pullover|glove)(\b|s\b).*',lname):
		attrList.append("apparel")
	elif re.match(r'.*\b(flag)(\b|s\b).*',lname):
		attrList.append("flags")
	elif re.match(r'.*\b(with pole|display pole|pole|flagpole)(\b|s\b).*',lname):
		attrList.append("flagpoles")
	elif re.match(r'.*\b(banner)(\b|s\b).*',lname):
		attrList.append("banner")
	elif re.match(r'.*\b(stand)(\b|s\b).*',lname):
		attrList.append("stands")
	elif re.match(r'.*\b(bracelet)(\b|s\b).*',lname):
		attrList.append("bracelet")
	else:
		attrList.append("others")

df=pd.read_csv("input/products.csv")
df=df[df.options.notnull()]
df.apply(lambda x: attr(x),axis=1)
df["attributes"]=attrList
df.to_csv("output/attributes.csv", index=False)