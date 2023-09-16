from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np


def feature_matrix_and_target_vector(df):
    print(df.columns)
    X = df.drop(["name", "mins", "apps", "traded"], axis=1).to_numpy()
    y = df["traded"].to_numpy()
    print(X.shape, y.shape)
