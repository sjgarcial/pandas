import pandas as pd

# se define la ruta del archivo csv

path='Sesion2\Online_Retail.csv'

retail_data=pd.read_csv(path,encoding='latin1')

print(type(retail_data))
print(retail_data.head(10))