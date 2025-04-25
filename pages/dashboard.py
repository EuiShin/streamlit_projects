import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt

# 데이터 셋
np.random.seed(42)
today = dt.date.today()
yesterday = dt.date.today()-dt.timedelta(days=1)
n = 365
register_temp = np.random.normal(1000, 200, n)
daily_data = pd.DataFrame(
    {
        'GMV':np.round(np.random.normal(500000000, 150000000, n),-2),
        'DAU':np.round(np.random.normal(70000, 20000, n),),
        'register':np.round(np.where(register_temp<0, 0, register_temp),)
    }
    , index = [dt.date.today()-dt.timedelta(days=i) for i in range(n)] 
)


st.title('실적 대시보드')

# 오늘의 지표
with st.container(border=True):
    st.write('### Today')
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "GMV", 
        f"{np.round(daily_data.loc[today]['GMV']/100000000,2)}억", 
        f"{np.round((daily_data.loc[today]['GMV']-daily_data.loc[yesterday]['GMV'])/100000000,2)}억", 
    )
    col2.metric(
        "DAU", 
        f"{np.round(daily_data.loc[today]['DAU']/10000,2)}만", 
        f"{np.round((daily_data.loc[today]['DAU'] - daily_data.loc[yesterday]['DAU'])/10000,2)}만", 
    )
    col3.metric(
        "회원가입", 
        f"{np.round(daily_data.loc[today]['register'],0)}", 
        f"{np.round((daily_data.loc[today]['register'] - daily_data.loc[yesterday]['register']),0)}", 
    )

# 추이 그래프
with st.container(border=True):
    st.write('### Trand')
    slider_val = st.slider(
        "기간을 설정하세요",
        value=(today-dt.timedelta(days=30), today),
        min_value=today-dt.timedelta(days=n),
        max_value=today
    )
    filter = (daily_data.index >= slider_val[0]) & (daily_data.index <= slider_val[1])
    tab1, tab2, tab3 = st.tabs(["GMV", "DAU", '회원가입'])
    tab1.bar_chart(daily_data.iloc[filter]['GMV'], height=250)
    tab2.bar_chart(daily_data.iloc[filter]['DAU'], height=250)
    tab3.bar_chart(daily_data.iloc[filter]['register'], height=250)
