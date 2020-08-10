import pandas as pandas
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt

from sklearn.databasets import load_iris

iris_data = load_iris()

iris_data.keys() #column headers
iris_data.feature_names #names of features
iris_data.target #Setosa as 0, Versicolor as 1, Virginica as 2
iris_data.target_names #Setosa, Versicolor, Virginica
iris_data.data.shape
iris_data.target.shape

from sklearn.model_selection import train_test_split
# Data is split into training and test data
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target)
x_train.shape
x_test.shape
y_train.shape
y_test.shape

# Because it's a classification problem, therefore LogisticRegression is used
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression() #Instance of Logstic Regression
lr.fit(x_train, y_train) #Fit function is used to train model
pred = lr.predict(x_test) #Prediction on test data
lr.score(x_train, y_train) #Check prediction on training data
lr.score(x_test, y_test) #Check prediction on test data

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, pred)
