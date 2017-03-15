import os
from six.moves import configparser as ConfigParser

###########################################################################
#Creating Directory
###########################################################################


def createDir(dir):
    currentDir=os.getcwd()
    try:
       os.makedirs(currentDir+'//'+dir)
    except:
       pass

###########################################################################
#Getting Config File Details
###########################################################################
def getConfigValue(section,key):
    config=ConfigParser.ConfigParser()
    config.read("config.ini")
    return config.get(section,key)