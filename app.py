import streamlit as st 
st.title("Restaurant Reviews")
import joblib 
text_model = joblib.load('reviews')
i = st.text_input("Enter the restaurant review")
y_pre = text_model.predict([i])
if st.button("Predict review") :
 if y_pre == [1] :
  st.title("You have got a positive review, congrats")
 else :
  st.title("You have got a negative review, try improving")
