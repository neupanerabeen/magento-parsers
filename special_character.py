#-*- coding: utf-8 -*-

import pandas as pd
import re

input_file="input/product_special_test.csv"
input_file="input/products.csv"

special_chars={'<li>':'\xef'}

def find_replace_special_char(row):
	desc = row["description"]
	new_desc = ""
	for char in desc:
		if ord(char) > 127:
			for sp_char in special_chars:
				if char == special_chars[sp_char]:
					new_desc+= sp_char

		else:
			new_desc+=char
	return new_desc


def remove_special_char(row):
	# print "yes"
	desc = row["description"]
	new_desc=""
	for char in desc:
		if ord(char)<127:
			new_desc+=char
	return new_desc

df=pd.read_csv(input_file)
df=df[df["price"].notnull() | df["sale-price"].notnull()]
df1=pd.DataFrame()
df1["sku"]=df["code"]
df1["description"]=df["caption"]
# df1.apply(find_replace_special_char, axis=1)
df1.description = df1.description.astype(str)
df1["description"]=df1.apply(find_replace_special_char, axis=1)
df1["description"]=df1.apply(remove_special_char, axis=1)
# df1=df1[df1["sku"]=="VFGSP6858"]
# print (df1.description)
df1.to_csv("no-spec-chars.csv", index=False)
