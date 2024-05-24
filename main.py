import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Coming Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

figure = px.line()
st.plotly_chart()