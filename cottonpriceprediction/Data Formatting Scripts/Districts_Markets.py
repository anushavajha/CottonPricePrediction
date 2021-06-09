import pandas as pd

df = pd.read_csv('CottonData.csv')
#Data Cleaning
df = df[df['Price'] > 0]
df = df[df['Price'] < 13000]
#DATE MERGING
df['Day']=df['Day'].apply(lambda x: '{0:0>2}'.format(x))
df['Month']=df['Month'].apply(lambda x: '{0:0>2}'.format(x))
df['Year'] = df['Year'].apply(str)
df['Day']=df['Day'].apply(str)
df['Month']=df['Month'].apply(str)
df['date'] = df['Year'].str.cat(df['Month'], sep ="-")
df['date'] = df['date'].str.cat(df['Day'], sep ="-")
df = df.drop(['Day', 'Month', "Year"], axis=1)
df_prop= pd.DataFrame()
df_prop['ds'] = pd.to_datetime(df["date"])
df_prop['y'] = df["Price"]
df_prop['State'] = df["State"]
df_prop['District'] = df["District"]
df_prop['Market'] = df["Market"]


# Encoding Categorical Columns
df_prop['State'] = df_prop['State'].astype('category')
df_prop['District'] = df_prop['District'].astype('category')
df_prop['Market'] = df_prop['Market'].astype('category')
df_prop['State_Code'] = df_prop['State'].cat.codes
df_prop['District_Code'] = df_prop['District'].cat.codes
df_prop['Market_Code'] = df_prop['Market'].cat.codes

#making dictionaries for categorical attributes
state_dict = pd.Series(df_prop.State_Code.values, index=df_prop.State).to_dict()
district_dict = pd.Series(df_prop.District_Code.values, index=df_prop.District).to_dict()
market_dict = pd.Series(df_prop.Market_Code.values, index=df_prop.Market).to_dict()
df_prop = df_prop.drop(['State', 'District', 'Market'], axis=1)

print(state_dict)