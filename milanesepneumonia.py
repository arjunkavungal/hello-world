import pandas as pd 
df = pd.read_csv('/kaggle/input/covid19-patient-precondition-dataset/covid.csv')
df.loc[df['date_died'] == '9999-99-99', 'death'] = 'False' 
df.loc[df['date_died'] != '9999-99-99', 'death'] = 'True' 
from sklearn.cluster import KMeans
X = df[['age','obesity']]
y = df['death']
kmeans = KMeans(n_clusters=2, random_state=0).fit(X,y)
