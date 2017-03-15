from Library import *
from six.moves import configparser as ConfigParser
import pandas as pd


class CrossProducts:

    def __init__(self):
        # reading config file
        self.productInput = getConfigValue('FilePaths', 'ProductInput')
        self.productImageOutput = getConfigValue('FilePaths','ProductImageOutput')

        # create empty data frame
        self.output=pd.DataFrame( )
        self.input = ""
        self.configFile="config.ini"
        self.mappingSection="ProductImagesMapping"
        self.image_list=[]

    def readConfigFile(self,section):
        config=ConfigParser.ConfigParser()
        config.read(self.configFile)
        #self.mapping=config.get(section,key)
        return dict(config.items(section))

    def readfile(self):
        # read input file. The path and filename is obtained from config file
        self.input = pd.read_csv(str(self.productInput))
        self.input = self.input[self.input["price"].notnull() & self.input["sale-price"].notnull()]

    def transform(self):
        configDict = self.readConfigFile(self.mappingSection)
        for key,value in configDict.items():
            try:
                self.output[key]=self.input[value]
            except Exception as e:
                print e
            finally:
                pass
        self.output=self.output[self.output["crosssell_skus"].notnull()]

    def modify(self):
    	self.output.apply(lambda x: self.getSku(x), axis=1)
        self.output["crosssell_skus"]=self.image_list
        del self.output["id"]
        del self.output["related_skus"]
    
    def getSku(self,row):
    	sku=row["sku"]
        id=row["id"]
        images=row["crosssell_skus"].split(" ")
        sk=""
        images = filter(None, images)
        for item in images:
            try:
                sk+= self.input["code"][self.input["id"]==item].iloc[0]+" "
            except:
                print "No product with id :"+item+ " of sku : "+sku
        #merged.append(pd.Series([item]))
        self.image_list.append(sk)

    def export(self):
        # generate final csv export
        self.output.to_csv("output/crossProducts.csv", index = False)

def main():
    pr = CrossProducts()
    pr.readfile()
    pr.transform()
    pr.modify()
    pr.export()


if __name__ == "__main__":
    main()