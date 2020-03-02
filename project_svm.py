# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:24:11 2018

@author: benny
"""

# Support Vector Machine (SVM)

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('indian_liver_patient.csv')
X = dataset.iloc[:, 0:9].values
y = dataset.iloc[:, 10].values
#X = dataset.drop('Dataset', axis=1)  
#y = dataset['Dataset']  
#encoding catagorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:,1] = labelencoder_X.fit_transform(X[:,1])

#take care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN",strategy = 'mean', axis=0)
imputer = imputer.fit(X)
X = imputer.transform(X)



# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'sigmoid')
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import classification_report, confusion_matrix  
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test,y_pred)

