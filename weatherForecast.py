#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib as jb

def weather(precipitation,max_temp,min_temp,wind):
    weather_data=pd.read_csv('weather.csv')
    X=weather_data.drop(columns=['date','weather'])
    y=weather_data['weather']
    #X
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    model=DecisionTreeClassifier()
    model.fit(X_train,y_train)
    # # predictions=model.predict(X_test)
    # # score=accuracy_score(y_test,predictions)
    # # score
    # # X
    jb.dump(model,"weatherforecast.joblib")
    model=jb.load("weatherforecast.joblib")
    #create a dataframe for predictions with the correct column
    input_data=pd.DataFrame([[precipitation,max_temp,min_temp,wind]],columns=X.columns)
    predictions=model.predict(input_data)
    return predictions



