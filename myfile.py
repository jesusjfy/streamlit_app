import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import time
st.title('Titulo del Proyecto')
st.write('Hola **como** estas')


appointment = st.slider(
 "Programe la asesoria:",
 value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)


d = st.date_input(
 "Fecha de cumpleaños",
 datetime.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)

option = st.selectbox(
 '¿Cómo desearía ser contactado/a?',
 ('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

df = pd.DataFrame(
 np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
 columns=['lat', 'lon'])