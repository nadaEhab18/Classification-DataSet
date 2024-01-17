# -*- coding: utf-8 -*-
"""Copy of FinnalDMYarab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sxM1PoPvnsWi8vGalKQc526t21ndCELo
"""

# Importing the libraries

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

# Read Dataset
df=pd.read_csv('train_and_test2.csv')
df.head()

len(df)

df.describe()

df.dtypes

df.isnull()

df.isnull().sum()

df.isnull().sum().sum()

!pip3 install -U scikit-learn

df = pd.read_csv('train_and_test2.csv')
X = df.iloc[:,:-1].values
X[:, 24:25]

# MISSING VALUES!!!

median_Embarked= df['Embarked'].median()

df['Embarked'].fillna(median_Embarked,inplace=True)

df.isnull().sum()

# Rename column
df.rename(columns={'2urvived':'Survived'},inplace=True)
df.head()

plt.figure(figsize=(12,10))
# we keep annot=True to make the values appear of df.corr() appear on the heatmap
sns.heatmap(df.corr(),annot=True,cmap=plt.cm.plasma)

df.drop(['Passengerid','zero','zero.1','zero.2','zero.3','zero.4','zero.5','zero.6','zero.7','zero.8','zero.9','zero.10','zero.11','zero.12','zero.13','zero.14','zero.15','zero.16','zero.17','zero.18'],axis=1,inplace=True)

plt.figure(figsize=(12,10))
# we keep annot=True to make the values appear of df.corr() appear on the heatmap
sns.heatmap(df.corr(),annot=True,cmap=plt.cm.plasma)

sns.pairplot(df)

df.columns

df.dtypes

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
print('x = \n',x)
print('**************************************')
print('y = \n',y)

#Encoding the dependent variable
df['Survived'] = df['Survived'].astype(str)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print("y =" , y)

# Split data to train & test

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X=df.drop(['Survived'],axis=1)
Y=df['Survived']
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.20,random_state=1)

print("x_train = " , X_train)
print('**************************************')
print("x_test =" , X_test)
print('**************************************')
print("y_train =" , y_train)
print('**************************************')
print("y_test =" , y_test)

df.head()

print(X_train)

print(X_train.shape)

len(df.Fare.unique())

#Feature scaling USING StandardScaler

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("x_train =" , X_train)
print('**************************************')
print("x_test =" , X_test)

print(X_scaled)

# Scalling USING MinMaxScaler()
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

print("x_train =", X_train)
print('**************')
print("x_test =", X_test)

print(X_scaled)

fig = plt.scatter(df.Age, df.Fare)
plt.xlabel('Age')
plt.ylabel('Fare')

fig = plt.hist(df.Age)

fig = plt.hist(df.Fare)

# Training K-NN Model
from sklearn.neighbors import KNeighborsClassifier
KN=KNeighborsClassifier(n_neighbors=5)
KN.fit(X_train,y_train)

import warnings
# Before making predictions, temporarily filter out the UserWarning
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)

    predictions = KN.predict(scaler.transform([[62, 45.0, 83.4750, 0, 1, 0, 1]]))

# Predicting the Test set Result  ==> yhat means y_predict
yhat=KN.predict(X_test)
print("Accuracy of K-Nearest Neighbor Model is:",accuracy_score(yhat,y_test))

import numpy as np

# Assuming yhat and y_test are Pandas Series
yhat_np = np.array(yhat).reshape(len(yhat), 1)
y_test_np = np.array(y_test).reshape(len(y_test), 1)

# Concatenate the arrays along axis 1
result = np.concatenate((yhat_np, y_test_np), axis=1)

print(result)
# trying to use the reshape method on a Pandas Series object (y_test).
#Unlike NumPy arrays, Pandas Series do not have a reshape method. Instead,
#you can convert the Series to a NumPy array using the values attribute and then use reshape.

len(result)

# Confusion_matrix

from sklearn.metrics import accuracy_score,confusion_matrix
cm=confusion_matrix(y_test,yhat)
print(cm)
accuracy_score(y_test,yhat)

import seaborn as sns
sns.heatmap(cm,annot=True,cmap=plt.cm.plasma)
plt.xlabel('Predict')
plt.ylabel('Actual')

import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))

# Assuming y_test containe actual values and y_pred_lr contains predicted values
plt.scatter(y_test,yhat,color='red',label='Predicted vs Actual')
plt.plot(y_test,y_test,'k--',lw=2) # Diagonal line for reference
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.legend
plt.show()

# visualizing confusion matrix
import seaborn as sns
ax = sns.heatmap(cm, annot=True, cmap='Blues')
ax.set_title('confusion matrix' + '\n\n')
ax.set_xlabel('\nPredicted values')
ax.set_ylabel('Actual values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['Survived','Not Survived'])
ax.yaxis.set_ticklabels(['Survived','Not Survived'])

## Display the visualization of the Confusion Matrix
plt.show()

# Training the Naive Bayes model on the training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train , y_train)

import warnings
# Before making predictions, temporarily filter out the UserWarning
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)

    predictions = KN.predict(scaler.transform([[62, 45.0, 83.4750, 0, 1, 0, 1]]))

import numpy as np

# Assuming yhat and y_test are Pandas Series
yhat_np = np.array(yhat).reshape(len(yhat), 1)
y_test_np = np.array(y_test).reshape(len(y_test), 1)

# Concatenate the arrays along axis 1
result = np.concatenate((yhat_np, y_test_np), axis=1)

print(result)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix , accuracy_score
cm = confusion_matrix(y_test, yhat)
print(cm)
accuracy_score(y_test, yhat)

# visualizing confusion matrix
import seaborn as sns
ax = sns.heatmap(cm, annot=True, cmap='Blues')
ax.set_title('confusion matrix' + '\n\n')
ax.set_xlabel('\nPredicted values')
ax.set_ylabel('Actual values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['Survived','Not Survived'])
ax.yaxis.set_ticklabels(['Survived','Not Survived'])

## Display the visualization of the Confusion Matrix
plt.show()

# Visualising the Test Set result
from matplotlib.colors import ListedColormap
x_set , y_set = scaler.inverse_transform(X_test) , y_test
x1 , x2 = np.meshgrid(np.arange(start = x_set[: ,0].min() - 10 , stop = x_set[: , 0].max() + 10 , step = 0.25),
                      np.arange(start = x_set[: ,1].min() - 1000 , stop = x_set[: , 1].max() + 1000 , step = 0.25))
plt.contourf(x1,x2,classifier.predict(scaler.transform(np.array([x1.ravel(),x2.ravel()]).T)).reshape(x1.shape),
            alpha = 0.75, cmap = ListedColormap(('red','green')))
plt.xlim(x1,min() , x1.max())
plt.xlim(x2.min() , x1.max())
for i , j in enumerate(np.unique(y_set)):
  plt.scatter(x_set[y_set == j,0], x_set[y_set == j , 1], c = ListedColormap(('red' , 'green'))(i), label = j)
plt.title('Naive Bayes (Test set)' )
plt.xlabel('')
plt.ylabel('')
plt.legend()

