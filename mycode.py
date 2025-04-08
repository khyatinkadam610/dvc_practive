import pandas as pd
import os

data = {'Name':['Alice','Bob','Charlie'],
        'Age':[77,45,23],
        'City':['Vadodara','Pune','chennaihehehe']}
df = pd.DataFrame(data)
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print("File daved succesfully at ",file_path)