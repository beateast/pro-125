import cv2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

X = np.load('image.npz', ['arr 0'] )
y = pd.read_csv('labels.csv'['labels'])
print(pd.Series(y).value_counts())
classes = ['a', 'b', 'c','d', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nclasses = len(classes)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 9, train_size = 7500, test_size = 2500)
X_train_scale = X_train/255.0
X_test_scale = X_test/255.0

print(X.loc[0])
print(y.loc[0])