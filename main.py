import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

images = {"Rain": "images/rain.png", "Clouds": "images/cloud.png", "Snow": "images/snow.png", "Clear": "images/clear.png"}

if place:
    # Get the temperature/sky data
    try:
        data = get_data(place, days)
        match option:
            case "Temperature":
                temp = [dict['main']['temp'] / 10 for dict in data]
                date = [dict['dt_txt'] for dict in data]
                figure = px.line(x=date, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
                st.plotly_chart(figure)
            case "Sky":
                sky_condition = [dict['weather'][0]['main'] for dict in data]
                image_paths = [images[condition] for condition in sky_condition]
                st.image(image_paths, width=115)
    except KeyError:
        st.info("No Such Place! Please Input Place Again...")


