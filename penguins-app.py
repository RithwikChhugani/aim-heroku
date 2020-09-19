import streamlit as st
import pandas as pd
import numpy as np
import pickle
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
	df = df.dropna()
	st.write(df.head())
	def user_input_features():
		pclass = st.sidebar.selectbox('Pclass', [0,1])
		sex = st.sidebar.selectbox('Sex', [0,1])
		age = st.sidebar.slider('Age', 0.42, 80.00,31.0)
		sibsp = st.sidebar.slider('SibSp', 0, 5, 2)
		parch = st.sidebar.slider('Parch',0,6,2)
		fare = st.sidebar.slider('Fare',0.0,2.0,513.0)
		embarked = st.sidebar.slider('Embarked',1,3,2)
		data = {'pclass': pclass, 'sex': sex,  'age': age, 'sibsp': sibsp,'parch':parch,'fare':fare,'embarked':embarked}
		features = pd.DataFrame(data, index=[0])
		return features

	df1 = user_input_features()

	# print info and description
	st.write(df.info())
	st.write(df.describe())
	st.subheader('User Input parameters')
	st.write(df1)
	
	
	

