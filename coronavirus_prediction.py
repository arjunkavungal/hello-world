import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('/kaggle/input/novel-corona-virus-2019-dataset/time_series_covid_19_confirmed.csv')
X = df.loc[:, ['3/25/20','3/26/20']]
ld = input("date?")
y = df[ld]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
reg = LinearRegression().fit(X_train, y_train)
#df[['3/24/20','3/25/20']]
y_pred = reg.predict(X_test)
df['3/28/20'] = pd.DataFrame(y_pred)
df
