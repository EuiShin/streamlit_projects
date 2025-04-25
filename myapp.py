# streamlit run c:/Users/sui94/streamlit_study/myapp.py
import streamlit as st

howami = st.Page(
    'pages/howami.py', 
    title='메인',
    default=True
)

page_color_choice = st.Page(
    'pages/font_color_choice.py', 
    title='글씨 색상 추천기'
)

dashboard = st.Page(
    'pages/dashboard.py', 
    title='대시보드'
)

map = st.Page(
    'pages/map.py', 
    title='지도'
)

# st.title('Reqest manager')

pg = st.navigation([
    howami, 
    page_color_choice,
    dashboard,
    map
])

pg.run()

