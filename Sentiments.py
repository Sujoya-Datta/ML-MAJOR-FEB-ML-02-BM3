import streamlit as st
import sklearn
import joblib
model = joblib.load('Tweets')
st.title('Tweets Classifier')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])

  
  
  
  
  
  
