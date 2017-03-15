from Library import *
from six.moves import configparser as ConfigParser
import pandas as pd

class AdvPrice:
	def __init__(self):
		self.productInput = getConfigValue('FilePaths', 'ProductInput')
		self.data=pd.Series()
		self.output=pd.DataFrame()
		self.skulist=[]
		self.pricelist=[]
		self.qtylist=[]	


	def readfile(self):
		# read input file. The path and filename is obtained from config file
		self.df = pd.read_csv(str(self.productInput))
		self.df=self.df[self.df["options"].isnull()]
		self.df = self.df[self.df["price"].notnull() & self.df["sale-price"].notnull()]

	def transform(self):
		self.output["sku"]=self.df["code"]
		self.output["price"]=self.df["sale-price"]
		self.output["qyp"]=self.output.price.map(lambda x : len(x)>5)
		self.output=self.output[self.output["qyp"]==True]
		del self.output["qyp"]
		del self.df
		self.output.apply(lambda x: self.go(x), axis=1)
		del self.output["price"]
		self.output=self.output[0:0]

		#self.output[data=self.data, columns=['sku','tier_price_qty','tier_price']]
		
	def modify(self):
		self.output["sku"]=self.skulist
		self.output["tier_price_website"]="All Websites [USD]"
		self.output["tier_price_customer_group"]="General"
		self.output["tier_price_qty"]=self.qtylist
		self.output["tier_price"]=self.pricelist

	def go(self,row):
		sku =row.sku
		price=row.price.split(" ")
		price.insert(0,1)
		count=0
		for index in xrange (2,len(price),2):
			if(len(price)%2==0):
				self.skulist.append(sku)
				self.qtylist.append(float(price[index]))
				p=float(price[index+1])/float(price[index])
				self.pricelist.append(p)
				count+=1
			else:
				print sku + " escaped"

	def export(self):
		# generate final csv export
		self.output.to_csv("output/AdvPrice.csv", index = False)

def main():
    pr = AdvPrice()
    pr.readfile()
    pr.transform()
    pr.modify()
    pr.export()


if __name__ == "__main__":
    main()