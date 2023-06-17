import pandas as pd

import streamlit as st

import predict


st.set_page_config(page_title="Определение стоимости квартир(ы)",
                   page_icon="🏠")

st.write("# Приложение для определения стоимости\
          квадратного метра жилплощади в г. Омске")

st.image('image.jpg')

st.markdown("С помощью нашего приложения Вы можете определить стоимость\
             квадратного метра жилой площади в квартире по интересующему Вас\
             адресу в г. Омске с использованием предварительно обученной\
             на данных о рынке недвижимости из открытых источников модели\
             на основе библиотеки Catboost. Для получения информации о\
             стоимости кв.м. недвижимости Вы можете воспользоваться\
             функцией предсказания по единственному адресу, который необходимо\
             в таком случае вручную ввести на странице 'single', либо\
             загрузить список интересующих Вас объектов на странице 'table'.")

