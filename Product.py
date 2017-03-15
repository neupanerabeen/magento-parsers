from Library import *
from six.moves import configparser as ConfigParser
import pandas as pd

class Products:

    def __init__(self):
        # reading config file
        self.productInput = getConfigValue('FilePaths', 'ProductInput')
        self.productOutput = getConfigValue('FilePaths','ProductOutput')

        # create empty data frame with default columns
        self.output=pd.DataFrame( )
        self.input = ""
        self.configFile="config.ini"
        self.mappingSection="MappingSimpleProducts"
        self.mappingDefaults="SettingDefaults"

    def readConfigFile(self,section):
        config=ConfigParser.ConfigParser()
        config.read(self.configFile)
        #self.mapping=config.get(section,key)
        return dict(config.items(section))

    def readfile(self):
        # read input file. The path and filename is obtained from config file
        self.input = pd.read_csv(str(self.productInput))
        self.input = self.input[self.input["price"].notnull() | self.input["sale-price"].notnull()]
        self.input =self.input[self.input["options"].isnull()]

    def transform(self):
        configDict = self.readConfigFile(self.mappingSection)
        for key,value in configDict.items():
            try:
                self.output[key]=self.input[value]
            except Exception as e:
                print e
            finally:
                pass
        confDict = self.readConfigFile(self.mappingDefaults)
        self.output["special_price"].fillna("", inplace=True)
        self.output["price"].fillna(self.output["special_price"], inplace=True)
        for key,value in confDict.items():
            try:
                if key in self.output.columns:
                    self.output[key].fillna(value, inplace=True)
                else:
                    self.output[key]=value
            except Exception as e:
                print e
            finally:
                pass

    def modify(self):
    	self.output.loc[self.output['tax_class_name']=="Yes",'tax_class_name']="Taxable Goods"
        self.output.loc[self.output['tax_class_name']=="No",'tax_class_name']="None"    
        self.output["price"]=self.output.price.map(lambda x:str(x))
        self.output["price"]=self.output.price.map(lambda x: x.split(" ")[0])
        self.output["special_price"]=self.output["special_price"].map(lambda x:str(x))
        self.output["special_price"]=self.output["special_price"].map(lambda x: x.split(" ")[0])
        
    def export(self):
        # generate final csv export
        self.output.to_csv(self.productOutput, index = False)

if __name__ == "__main__":
	pr = Products()
	pr.readfile()
	pr.transform()
	pr.modify()
	pr.export()
