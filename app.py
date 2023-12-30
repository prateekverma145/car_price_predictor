import streamlit as st
import numpy as np
import pickle 


st.sidebar.markdown("<h1 style='text-align: left; color: white;'>Car Price Prediction</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: left; color: white;'>This app predicts the **MSRP** of a car based on its specifications</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: left; color: white;'>A simple web app to predict the GDP per capita of a country</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: Green;'>Made by Prateek Verma</h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: white;'>Github:<a href='https://github.com/prateekverma145'>prateekverma145</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: white;'>LinkedIn:<a href='https://www.linkedin.com/in/prateek-verma-2a202b287'>prateek-verma</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: white;'>Dataset:<a href='https://www.kaggle.com/datasets/hellbuoy/car-price-prediction'>prateekverma14</a></h4>", unsafe_allow_html=True)
model=pickle.load(open('model.sav','rb'))
# input parameters
# drivewheel	wheelbase	carlength	carwidth	carheight	curbweight	enginesize	boreratio	horsepower	peakrpm	citympg	highwaympg
st.subheader('Select the values to predict the price')
a=st.selectbox('Drive Wheel',('fwd','rwd'))
if a=='fwd':
    a=0
else:
    a=1
    
b=st.slider('Wheel Base',50.0,150.0,step=0.2)
c=st.slider('Car Length',120.0,270.0,step=0.2)
d=st.slider('Car Width',40.0,150.0,step=0.2)
e=st.slider('Car Height',30.0,100.0,step=0.2)
f=st.slider('Curb Weight',1000.0,5000.0,step=10.5)
g=st.slider('Engine Size',50.0,500.0,step=2.2)
h=st.slider('Bore Ratio',1.0,5.0,step=0.1)
i=st.slider('Horse Power',30.0,500.0,step=1.0)
j=st.slider('Peak RPM',2000.0,10000.0,step=100.0)
k=st.slider('City MPG',10.0,100.0,step=0.2)
l=st.slider('Highway MPG',10.0,100.0,step=0.2)
# 7988.0 is mean and 5118 is std of price column in dataset used
arr=np.array([a,b,c,d,e,f,g,h,i,j,k,l]).reshape(1,-1)
if st.button('Predict'):
    st.subheader(f'The predicted price of the car is {"{:.2f}".format(model.predict(arr)[0]*7988+5118)}')

