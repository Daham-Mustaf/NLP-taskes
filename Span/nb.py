from __future__ import print_function, division
from builtins import range
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np

data = pd.read_csv('spambase.data').values
np.random.shuffle(data)

X = data[:,:48]
Y = data[:,-1]

# split the dataset into training and testing sets.
Xtrain = X[:-100,] # selects all rows up to the last 100 rows of X as the training set input features.
Ytrain = Y[:-100,]
Xtest = X[-100:,]  #selects the last 100 rows of X as the testing set input features.
Ytest = Y[-100:,]

model = MultinomialNB()
model.fit(Xtrain, Ytrain)
print("Classification rate for NB:", model.score(Xtest, Ytest))

##### you can use ANY model! #####
from sklearn.ensemble import AdaBoostClassifier

model = AdaBoostClassifier()
model.fit(Xtrain, Ytrain)
print("Classification rate for AdaBoost:", model.score(Xtest, Ytest))