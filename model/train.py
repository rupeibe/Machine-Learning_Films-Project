
import pandas as pd

df = pd.read_csv(r"..\data\processed\peliculas_analisis_ML.csv",index_col=0)

X = df.drop('puntuacion', axis=1)
y = df['puntuacion']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.15,
                                                    random_state=42)

from catboost import CatBoostRegressor

seed = 42

CatBoost_Model = CatBoostRegressor(random_state= seed, verbose = False, learning_rate= 0.1, max_depth= 8, n_estimators= 300)

from sklearn.ensemble import BaggingRegressor

Bagging_Model = BaggingRegressor(estimator=CatBoost_Model, n_estimators=10, random_state=seed)
Bagging_Model.fit(X_train, y_train)

import pickle

# Save the trained model
with open(r'new_model.pkl', 'wb') as file:
    pickle.dump(Bagging_Model, file)