import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.header('Welcome to our Titanic Streamlit Web App')
st.subheader('''
	The page is divied in two categories:
		1. PowerBI report on Titanic dataset
		2. Data preprocessing and predictions
	''')

options = st.selectbox('Please Select',['PowerBI','Preprocessing & predictions'])

st.write('\n\n')

if options == 'PowerBI':
	st.markdown("""<iframe width="600" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiMjUyNDQ2YTYtYWY2Yy00NWU0LWJmYTMtOGY2YjBhZjI5NTM2IiwidCI6IjZkYjU5OTA5LTYyMjYtNDQ3My05MDYxLWJhZTNjNjRiY2I4NCIsImMiOjEwfQ%3D%3D&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>""",unsafe_allow_html=True)

else:
	df = pd.read_csv('titanic.csv')
	st.write(df.head())
	df = df.drop(['Name','PassengerId','Ticket','Cabin'],axis=1)
	labelencoder = LabelEncoder()
	df['Pclass'] = labelencoder.fit_transform(df['Pclass'])
	df['Survived'] = labelencoder.fit_transform(df['Survived'])
	df['Embarked'] = labelencoder.fit_transform(df['Embarked'])
	df['Sex'] = labelencoder.fit_transform(df['Sex'])
	

