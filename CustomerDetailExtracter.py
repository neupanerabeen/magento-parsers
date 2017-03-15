from Library import *
import pandas as pd
import numpy as np

lastEmail = "aa"

###########################################################################
#Getting the Core Customer Details
###########################################################################
def getCustomerDetails(sourceDataFrame):
    #customerDetailsFile = getConfigValue('FilePaths', 'OutputCustomerDetailsFile')
    outputFileColumns = ['email','_website','_store','confirmation','created_at','created_in','disable_auto_group_change','dob',
                         'firstname','gender','group_id','lastname','middlename','password_hash','prefix','rp_token',
                         'rp_token_created_at','store_id','suffix','taxvat','website_id','password']
    customerDetailsDataFrame = pd.DataFrame(columns=outputFileColumns)

    #Mapping From Source File to Target CSV file
    customerDetailsDataFrame['email']=sourceDataFrame['Email Address']
    customerDetailsDataFrame['_website'] = 'base'
    customerDetailsDataFrame['_store'] = 'default'
    customerDetailsDataFrame['confirmation'] = ''
    customerDetailsDataFrame['created_at'] = sourceDataFrame['Registration Date']
    customerDetailsDataFrame['created_in'] = 'Default Store View'
    customerDetailsDataFrame['disable_auto_group_change'] = '0'
    customerDetailsDataFrame['dob'] = ''
    customerDetailsDataFrame['firstname'] = sourceDataFrame['First Name']
    customerDetailsDataFrame['gender'] = ''
    customerDetailsDataFrame['group_id'] = '1'
    customerDetailsDataFrame['lastname'] = sourceDataFrame['Last Name']
    customerDetailsDataFrame['middlename'] = ''
    customerDetailsDataFrame['password_hash'] = ''
    customerDetailsDataFrame['prefix'] = ''
    customerDetailsDataFrame['rp_token'] = ''
    customerDetailsDataFrame['rp_token_created_at'] = ''
    customerDetailsDataFrame['store_id'] = '1'
    customerDetailsDataFrame['suffix'] = ''
    customerDetailsDataFrame['taxvat'] = ''
    customerDetailsDataFrame['website_id'] = '1'
    customerDetailsDataFrame['password'] = ''

    return customerDetailsDataFrame

###########################################################################
# Getting Customer Secondary Shipping Address Details
###########################################################################
def getCustomerSameShipBillAddressDetails(df):
    outputFileColumns = ['_website','_email','_entity_id','city','company','country_id','fax','firstname','lastname','middlename',
                         'postcode','prefix','region','region_id','street','suffix','telephone','vat_id','vat_is_valid',
                         'vat_request_date','vat_request_id','vat_request_success','_address_default_billing_',
                         '_address_default_shipping_']
    customerAddressDetailsDataFrame = pd.DataFrame(columns=outputFileColumns)

    #Mapping Comman data
    sourceDataFrame=df[df["isShipBillSame"]==0]
    customerAddressDetailsDataFrame['_website'] = 'base'
    customerAddressDetailsDataFrame['_email'] = sourceDataFrame['Email Address']
    customerAddressDetailsDataFrame['fax'] = ''
    customerAddressDetailsDataFrame['firstname'] = sourceDataFrame['First Name']
    customerAddressDetailsDataFrame['lastname'] = sourceDataFrame['Last Name']
    customerAddressDetailsDataFrame['middlename'] = ''
    customerAddressDetailsDataFrame['prefix'] = ''
    customerAddressDetailsDataFrame['suffix'] = ''
    customerAddressDetailsDataFrame['vat_id'] = ''
    customerAddressDetailsDataFrame['telephone'] = sourceDataFrame['Phone Number']
    customerAddressDetailsDataFrame['_entity_id'] = '1'
    customerAddressDetailsDataFrame['city'] = sourceDataFrame['Ship City']
    customerAddressDetailsDataFrame['company'] = sourceDataFrame['Ship Company']
    customerAddressDetailsDataFrame['country_id'] = sourceDataFrame['Ship Country']
    customerAddressDetailsDataFrame['postcode'] = sourceDataFrame['Ship Zip']
    customerAddressDetailsDataFrame['region'] = sourceDataFrame['Ship State']
    customerAddressDetailsDataFrame['street'] = sourceDataFrame['Ship Address1']+'\n'+sourceDataFrame['Ship Address2']
    customerAddressDetailsDataFrame['_address_default_billing_'] = '1'
    customerAddressDetailsDataFrame['_address_default_shipping_'] = '1'
    #print(customerAddressDetailsDataFrame.shape)
    return customerAddressDetailsDataFrame

def getCustomerDiffShipBillAddressDetails(df):
    outputFileColumns = ['_website','_email','_entity_id','city','company','country_id','fax','firstname','lastname','middlename',
                         'postcode','prefix','region','region_id','street','suffix','telephone','vat_id','vat_is_valid',
                         'vat_request_date','vat_request_id','vat_request_success','_address_default_billing_',
                         '_address_default_shipping_']
    
    sourceDataFrame=df[df["isShipBillSame"]==1]
    customerShippingAddressDetailsDataFrame = pd.DataFrame(columns=outputFileColumns)
    customerBillingingAddressDetailsDataFrame = pd.DataFrame(columns=outputFileColumns)

    #Mapping Comman data
    customerShippingAddressDetailsDataFrame['_website'] = 'base'
    customerShippingAddressDetailsDataFrame['_email'] = sourceDataFrame['Email Address']
    customerShippingAddressDetailsDataFrame['fax'] = ''
    customerShippingAddressDetailsDataFrame['firstname'] = sourceDataFrame['First Name']
    customerShippingAddressDetailsDataFrame['lastname'] = sourceDataFrame['Last Name']
    customerShippingAddressDetailsDataFrame['middlename'] = ''
    customerShippingAddressDetailsDataFrame['prefix'] = ''
    customerShippingAddressDetailsDataFrame['suffix'] = ''
    customerShippingAddressDetailsDataFrame['vat_id'] = ''
    customerShippingAddressDetailsDataFrame['telephone'] = sourceDataFrame['Phone Number']
    customerShippingAddressDetailsDataFrame['_entity_id'] = '1'
    customerShippingAddressDetailsDataFrame['city'] = sourceDataFrame['Ship City']
    customerShippingAddressDetailsDataFrame['company'] = sourceDataFrame['Ship Company']
    customerShippingAddressDetailsDataFrame['country_id'] = sourceDataFrame['Ship Country']
    customerShippingAddressDetailsDataFrame['postcode'] = sourceDataFrame['Ship Zip']
    customerShippingAddressDetailsDataFrame['region'] = sourceDataFrame['Ship State']
    customerShippingAddressDetailsDataFrame['street'] = sourceDataFrame['Ship Address1']+'\n'+sourceDataFrame['Ship Address2']
    customerShippingAddressDetailsDataFrame['_address_default_billing_'] = ''
    customerShippingAddressDetailsDataFrame['_address_default_shipping_'] = '1'

    #Billing
    customerBillingingAddressDetailsDataFrame['_website'] = 'base'
    customerBillingingAddressDetailsDataFrame['_email'] = sourceDataFrame['Email Address']
    customerBillingingAddressDetailsDataFrame['fax'] = ''
    customerBillingingAddressDetailsDataFrame['firstname'] = sourceDataFrame['First Name']
    customerBillingingAddressDetailsDataFrame['lastname'] = sourceDataFrame['Last Name']
    customerBillingingAddressDetailsDataFrame['middlename'] = ''
    customerBillingingAddressDetailsDataFrame['prefix'] = ''
    customerBillingingAddressDetailsDataFrame['suffix'] = ''
    customerBillingingAddressDetailsDataFrame['vat_id'] = ''
    customerBillingingAddressDetailsDataFrame['telephone'] = sourceDataFrame['Phone Number']
    customerBillingingAddressDetailsDataFrame['_entity_id'] = '2'
    customerBillingingAddressDetailsDataFrame['city'] = sourceDataFrame['Bill City']
    customerBillingingAddressDetailsDataFrame['company'] = sourceDataFrame['Bill Company']
    customerBillingingAddressDetailsDataFrame['country_id'] = sourceDataFrame['Bill Country']
    customerBillingingAddressDetailsDataFrame['postcode'] = sourceDataFrame['Bill Zip']
    customerBillingingAddressDetailsDataFrame['region'] = sourceDataFrame['Bill State']
    customerBillingingAddressDetailsDataFrame['street'] = sourceDataFrame['Bill Address1']+'\n'+sourceDataFrame['Bill Address2']
    customerBillingingAddressDetailsDataFrame['_address_default_billing_'] = '1'
    customerBillingingAddressDetailsDataFrame['_address_default_shipping_'] = ''
    return customerShippingAddressDetailsDataFrame,customerBillingingAddressDetailsDataFrame


if __name__ == "__main__":
    print("Task started!\n")
    #Reading Config file
    # lastEmail="asdf"

    SourceCsvFile= getConfigValue('FilePaths','InputSourceCustomerFile')

#    customerOutput=getConfigValue('FilePaths','OutputCustomerDetailsFile')
#    addressOutput = getConfigValue('FilePaths', 'OutputCustomerAddressFile')

    sourceDataFrame = pd.read_csv(SourceCsvFile)
    sourceDataFrame["Bill Address2"].fillna("###", inplace=True)
    sourceDataFrame["Ship Address2"].fillna("###", inplace=True)
    
    #Getting Basic Customer Details along with Shipping Address
    sourceDataFrame["shippingAddress"]=sourceDataFrame["Ship Address1"]+ " "+sourceDataFrame["Ship Address2"]
    sourceDataFrame["billingAddress"]=sourceDataFrame["Bill Address1"]+" "+ sourceDataFrame["Bill Address2"]
    sourceDataFrame["isShipBillSame"]=np.where(sourceDataFrame["shippingAddress"]==sourceDataFrame["billingAddress"],0,1)

    # this function creates and dumps the csv output.
    
    customer=getCustomerDetails(sourceDataFrame)
#    customer['newEmail'] = map(lambda x: x.upper(), customer['email'])
#    customer=customer.sort('newEmail')
#    customer=customer.drop_duplicates('newEmail')
    customer['lastname'].fillna("[_LastName]", inplace=True)
    customer['lastname'].replace('0',"[_LastName]", inplace=True)
#    del customer['newEmail']
    customer.to_csv("output/CustomerDetails.csv",index=False)
    
    #Getting Shipping Address
    customerShippBillSameAddressDataFrame=getCustomerSameShipBillAddressDetails(sourceDataFrame)

    # Getting Shipping Address
    customerShippingAddressDataFrame,customerBillingAddressDataFrame = getCustomerDiffShipBillAddressDetails(sourceDataFrame)

    customerAllAddressDetails = pd.concat([customerShippBillSameAddressDataFrame,customerShippingAddressDataFrame,customerBillingAddressDataFrame])
    customerAllAddressDetails['street'] = customerAllAddressDetails['street'].str.replace("\n###","")
    customerAllAddressDetails=customerAllAddressDetails.sort_values(['_email'])
    # print customerAllAddressDetails["_email"]
    # customerAllAddressDetails.apply(lambda x : merge_orders(x), axis = 1)
    # exit()
    customerAllAddressDetails['_website']="base"
    customerAllAddressDetails['lastname'].fillna('[_lastname]',inplace=True)
    customerAllAddressDetails['lastname'].replace('0',"[_lastname]",inplace=True)
    customerAllAddressDetails['telephone'].fillna("[_telephone]",inplace=True)
    customerAllAddressDetails['city'].fillna('[_city]',inplace=True)
    customerAllAddressDetails['postcode'].fillna('[_Postcode]',inplace=True)
    customerAllAddressDetails['street'].fillna('[_street]',inplace=True)

    customerAllAddressDetails.to_csv("output/OutputAddress.csv", index=False)
    print("Output printed as \n 1. For Address: \" OutputAddress.csv\' \n 2. For customer data: \" customerDetailsFile.csv\" \n Find the files and import to Magento!")