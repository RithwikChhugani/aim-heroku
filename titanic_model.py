import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.model_selection import train_test_split

df = pd.read_csv('titanic.csv')
df = df.drop(['Name','PassengerId','Ticket','Cabin'],axis=1)
# dropping null values
df = df.dropna() 

y = df['Survived']
X = df.iloc[:,1:]

# split into train test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# making model and fitting
log_reg = LogisticRegression()
log_reg.fit(X_train,y_train)

pickle.dump(log_reg,open('titanic_clf.pkl','wb'))