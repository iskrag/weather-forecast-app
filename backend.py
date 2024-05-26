import requests
import streamlit as st

API_KEY = 'dde32aae73ddeb210ee8ec4d8ccf2ee8'


def get_data(place, days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    st.write('Please enter a valid city name.')
    nr_values = 8*days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Tokyo', days=3))
