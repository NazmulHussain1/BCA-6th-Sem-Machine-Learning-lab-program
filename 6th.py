#Write a python program to handle missing data,encode categorial variabls and perform feature scalling
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

#Create a Dummy data
data={'Age':[25,30, None, 28,35],
      'Gender':['Female','Male','Male','Female','Male'],
      'Income':[50000,60000,45000, None, 70000]
}
df=pd.DataFrame(data)

#Handling missing data
imputer=SimpleImputer(strategy='mean')
df[['age','Income']]=imputer.fit_transform(df[['Age','Income']])

#print data after handling missing values
print("data after handling missing values:")
print(df)

#Encoding categorical variables
encoder=OneHotEncoder()
encoded_data=encoder.fit_transform(df[['Gender']]).toarray()


#print data after categorical encoding
encoded_df  =  pd.DataFrame(encoded_data,  columns=encoder.get_feature_names_out(['Gender']))
print("\nData after categorical encoding:")
print(encoded_df)



#feature scalling
scaler=StandardScaler()
scaled_data=scaler.fit_transform(df[['Age','Income']])

#print data after feature Scaling
scaled_df=pd.DataFrame(scaled_data,columns=['Scaled Age','Scaled Income'])
print("\ndata after feature scaling:")
print(scaled_df)







