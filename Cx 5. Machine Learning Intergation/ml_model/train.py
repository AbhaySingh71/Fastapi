import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Cx 5. Machine Learning Intergation\housing.csv').iloc[:, :-1].dropna()
print("Read the data")

X = df.drop('median_house_value', axis=1)
y = df['median_house_value']

print("Split the data")

lr = LinearRegression()
lr.fit(X, y)
print("Trained the model")

joblib.dump(lr, 'Cx 5. Machine Learning Intergation\ml_model\model.joblib')
print("Saved the model")