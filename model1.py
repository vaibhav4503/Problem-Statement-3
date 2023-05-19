import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import pickle

df = pd.read_csv('Churn.csv')

#preprocessing

#chnage spaces to zeros
df['TotalCharges'].replace(' ', 0, inplace=True)

#change the dtype
df['TotalCharges'] = df['TotalCharges'].astype('float64')

#encoding of categorical values
df.replace('No phone service','No', inplace=True)
df.replace('No internet service','No', inplace=True)

#convert yes to 1 and no to 0
category_convert = {'No': 0, 'Yes': 1}
df.replace(category_convert, inplace=True)

#convert gender
df['gender'].replace({'Male':1, 'Female':0}, inplace=True)

#one hot encoding
ohe_cols = ['PaymentMethod','Contract','InternetService']

df = pd.get_dummies(df, prefix= ohe_cols, columns= ohe_cols, drop_first=True)

#drop unique identifier column
df.drop(columns='customerID', inplace=True)

#set X and y
X = df.drop(['Churn'], axis=1)
y = df['Churn']

#split into train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#model building
rf = RandomForestClassifier(random_state= 123, n_estimators=350, max_depth=10)
rf.fit(X_train, y_train)

y_pred=rf.predict(X_test)
score=accuracy_score(y_test,y_pred)

print('Score is',score)

pickle.dump(rf, open('model.pkl','wb'))
