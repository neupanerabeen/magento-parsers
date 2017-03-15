import pandas as pd

# read tge customer csv
input_df=pd.read_csv("categories.csv")
# read magento export here !left
magento_df = pd.read_csv("magento_export.csv")
# dictionary for cleaning categories
cat_replace = {'POW/MIA':'POW##MIA', 'Holiday & Seasonal Flags/Banners':'Holiday & Seasonal Flags##Banners'}

def update_category(row):
	categories = str(row["categories"])
	for cat_rep in cat_replace:
		if cat_rep in categories:
			categories = categories.replace(cat_rep, cat_replace[cat_rep])
	newCat = ""
	categories= categories.split(',')
	for category in categories:
		newCat+= "Default Category/"+category+","
	newCat = newCat.strip(",")
	return newCat

def add_categories(row):
	sku = row["sku"].split("_")[0]
	category = input_df["categories"][input_df["sku"] == sku]
	newCat = ""
	if sku in skuList:
		newCat = input_df[input_df["sku"] == sku]["categories"].tolist()[0]
	else:
		newCat = row["categories"]
	return newCat

input_df = input_df[["code","sections"]]
input_df.columns = ["sku", "categories"]
input_df["categories"] = input_df.apply(update_category,axis=1)
skuList = input_df["sku"].tolist()

magento_df = magento_df[["sku","categories"]].astype(str)
magento_df["categories"] = magento_df.apply(add_categories, axis = 1)
magento_df.to_csv("newCategories.csv", index=False)
# print sku_list