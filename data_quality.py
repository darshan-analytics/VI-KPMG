import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as date
import datetime
import numpy as np

desired_width=320

pd.set_option('display.width', desired_width)


pd.set_option('display.max_columns',10)
df = pd.read_excel('KPMG_VI_New_raw_data_update_final.xlsx', sheet_name= "NewCustomerList")

for col in df.columns:
    print(col)

#here we get column name as unnamed so will update it


df.rename(columns={"Note: The data and information in this document is reflective of a hypothetical situation and client. This document is to be used for KPMG Virtual Internship purposes only. ":"first_name"}, inplace = True)
#df.drop(['Note_given_by_kpmg'],axis=1,inplace=True)

print(100 * '-')


df.rename(columns={"Unnamed: 1":"Last_name", "Unnamed: 2":"gender", "Unnamed: 3":"past_3_years_bike_related_purchases","Unnamed: 4":"DOB", "Unnamed: 5":"job_title", "Unnamed: 6":"job_industry_category","Unnamed: 7":"wealth_segment",
                   "Unnamed: 8":"deceased_indicator", "Unnamed: 9":"owns_car", "Unnamed: 10":"tenure", "Unnamed: 11":"address", "Unnamed: 12":"postcode", "Unnamed: 13":"state", "Unnamed: 14":"country", "Unnamed: 15":"property_valueation","Unnamed: 21":"Rank","Unnamed: 22":"Value"}, inplace=True)

#as we have replaced the names of the columns now will skip first line as it was the Note and start from the second columns

df = df.iloc[1::]

#now will drop the Unnamed COlumns which are found to be extra

df.drop(["Unnamed: 16","Unnamed: 17","Unnamed: 18","Unnamed: 19","Unnamed: 20"], axis =1, inplace= True)

'''print(df.columns[df.isna().any()])

print('Last_name missing values',df['Last_name'].isna().sum())
print('DOB missing values',df['DOB'].isna().sum())
print('job_title',df['job_title'].isna().sum())
print('job_industry_category',df['job_industry_category'].isna().sum())'''

#double checking if any missing value o be extra sure
print(df.isna().sum())

plt.bar(('Last_name','DOB','job_title','job_industry_category'),(29,17,106,165))
plt.xlabel("Columns in which we have empty values")
plt.ylabel("Missing Values")
plt.show()

print(100 * '-')
#finding unique gender counts in the dataset
print(df['gender'].value_counts())
#checking gender-wise car purchase report
print(df[df['owns_car']=='Yes'].gender.value_counts())
plt.figure()
labels = "Female", "Male", "U"
size = [261, 225, 7]
explode = (0,0,0.08)
plt.pie(size, explode= explode, labels = labels, startangle= 90, shadow = True, autopct='%1.1f%%')
plt.axis('equal')
plt.show()


#finding affluencywise
print(df['wealth_segment'].value_counts())
#checking affluencywise car purchase report
print(df[df['owns_car']=='Yes'].wealth_segment.value_counts())
plt.figure()
plt.bar("1",254, label="Mass customer")
plt.bar("2",125, label="Affluent Customer")
plt.bar("3",114, label="High net worth")
plt.legend()
plt.show()

#finding statewise
print(df['state'].value_counts())
#checking statewise car purchase report
print(df[df['owns_car']=='Yes'].state.value_counts())

plt.figure()
plt.bar("1",234, label="NSW")
plt.bar("2",134, label="VIC")
plt.bar("3",125, label="QLD")
plt.legend()
plt.show()

transaction = pd.read_excel('KPMG_VI_New_raw_data_update_final.xlsx', sheet_name= "Transactions")

#now will name the columns of the transaction set as well
transaction.rename(columns={"Note: The data and information in this document is reflective of a hypothetical situation and client. This document is to be used for KPMG Virtual Internship purposes only. ":"transactions_id"}, inplace = True)

transaction.rename(columns={"Unnamed: 1":"product_id","Unnamed: 2":"customer_id", "Unnamed: 3":"transaction_date","Unnamed: 4":"online_order", "Unnamed: 5":"order_status", "Unnamed: 6":"brand","Unnamed: 7":"product_line",
                   "Unnamed: 8":"product_class", "Unnamed: 9":"product_size", "Unnamed: 10":"list_price", "Unnamed: 11":"standard_cost", "Unnamed: 12":"product_first_sold_date"}, inplace=True)

for col in transaction.columns:
    print(col)

transaction = transaction.iloc[1:]
#transaction.drop(["first_name"], axis = 1, inplace= True)

#print(transaction.columns[transaction.isna().any()].tolist())

print(100 *'-')

#check_sum of missing values
print(transaction.isna().sum())

plt.figure()
plt.bar("1",360, label="online_order")
plt.bar("2",197, label="product_line")
plt.bar("3",197, label="brand")
plt.bar("4",197, label="product_class")
plt.bar("5",197, label="product_size")
plt.bar("6",197, label="standard_cost")
plt.bar("7",197, label="product_first_sold_date")
plt.legend()
plt.show()

print(200 * "-")

#taking customer demographic data
customer_demographic = pd.read_excel('KPMG_VI_New_raw_data_update_final.xlsx', sheet_name= "CustomerDemographic")

customer_demographic.rename(columns={"Note: The data and information in this document is reflective of a hypothetical situation and client. This document is to be used for KPMG Virtual Internship purposes only. ":"customer_id"}, inplace = True)

customer_demographic.rename(columns={"Unnamed: 1":"first_name","Unnamed: 2":"last_name", "Unnamed: 3":"gender","Unnamed: 4":"past_3_years_bike_related_purchases", "Unnamed: 5":"DOB", "Unnamed: 6":"job_title","Unnamed: 7":"job_industry_category",
                   "Unnamed: 8":"wealth_segment", "Unnamed: 9":"deceased_indicator", "Unnamed: 10":"default", "Unnamed: 11":"owns_car", "Unnamed: 12":"tenure"}, inplace=True)

#printing all the columns in these sheet

for col in customer_demographic.columns:
    print(col)

customer_demographic = customer_demographic.iloc[1:]

#dropping default column as it contains unnecessary data

customer_demographic.drop(["default"], axis = 1, inplace= True)

#checking the columns with none values over the sheet
print(customer_demographic.isna().sum())

customer_demographic.dropna(inplace = True)


#in job industry checking how many unique industries are there and removing the none values
print(customer_demographic["job_industry_category"].isna().sum())


print(customer_demographic["job_industry_category"].value_counts())

#finally printing the car purchased along with industry
print(customer_demographic[customer_demographic['owns_car']=='Yes'].job_industry_category.value_counts())
plt.figure()
plt.bar("1",359, label="finance")
plt.bar("2",330, label="manufacturing")
plt.bar("3",257, label="health")
plt.bar("4",151, label="retail")
plt.bar("5",121, label="property")
plt.bar("6",64, label="IT")
plt.bar("7",57, label="agriculture")
plt.bar("8",51, label= "entertainment")
plt.bar("9",31, label="Telecom")
plt.legend()
plt.show()