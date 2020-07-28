from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
import pandas as pd

if __name__== '__main__':
    houses = pd.read_csv('data/kc_house_data.csv')

    X = houses[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement']]
    y = houses['price']

    lr = LinearRegression()
    lr.fit(X, y)

    joblib.dump(lr, 'model.joblib')


