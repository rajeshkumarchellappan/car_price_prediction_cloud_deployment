import pandas as pd
df = pd.read_csv('car_dataset_deploy')
print(df.head())
y = df.Selling_Price
X = df.drop(['Unnamed: 0', 'Selling_Price'], axis=1)
print(X.head())
print(y.head())

# Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model building

import sklearn.ensemble
extr = sklearn.ensemble.ExtraTreesRegressor()
extr.fit(X_train, y_train)
y_pred_extr = extr.predict(X_test)
y_pred_extr1 = extr.predict([[8, 5.59, 27000, 0, 0, 1, 0, 1]])
print(y_pred_extr1)
import pickle
pickle.dump(extr,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

print(model)