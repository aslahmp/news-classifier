import streamlit as st
import joblib

model=joblib.load('news-classification-model.pkl')
news_labels={'0':'Technical','1':'Business','2':'Sports','3':'Entertainment','4':'Politics'}
st.title('News Classification')
ip = st.text_area("Enter the News")
if st.button('Predict'):
  predicted_label=model.predict([ip])[0]
  predicted_news_label=news_labels[str(predicted_label)]
  st.title("Predicted News Category is: "+predicted_news_label)
