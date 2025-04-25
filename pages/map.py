import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


st.title(' OO세권 찾기')
st.write('''
    다양한 체인 점포를 선택하고 한 곳에 모여있는 곳을 찾아봐요.
''')

st.pydeck_chart(pdk.Deck(
    map_style='road',
    initial_view_state=pdk.ViewState(
        latitude=37.57,
        longitude=126.97698,
        zoom=13,
    ),
    # layers=[
    #     pdk.Layer(
    #        'HexagonLayer',
    #        data=chart_data,
    #        get_position='[lon, lat]',
    #        radius=200,
    #        elevation_scale=4,
    #        elevation_range=[0, 1000],
    #        pickable=True,
    #        extruded=True,
    #     ),
    #     pdk.Layer(
    #         'ScatterplotLayer',
    #         data=chart_data,
    #         get_position='[lon, lat]',
    #         get_color='[200, 30, 0, 160]',
    #         get_radius=200,
    #     ),
    # ],
))