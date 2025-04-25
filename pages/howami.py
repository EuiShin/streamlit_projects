# streamlit run c:/Users/sui94/streamlit_study/app.py
import streamlit as st

def dict_to_badge(dict):
    badge_str = ''
    for key, value in dict.items():
        badge_str += f':{value}-badge[{key}]  '
    return badge_str


st.write('# 신의 데이터분석가')
st.write('데이터와 기술을 통해 비즈니스 문제를 해결합니다.')

st.header("Skills", divider=True)
skills = {
    'python' : 'blue',
    'SQL' : 'red', 
    '데이터시각화' : 'green',
    'Redash' : 'red',
    'GoogleSheets' : 'orange',
    '사업기획' : 'violet'
}
st.markdown(dict_to_badge(skills))



st.header("학업", divider='rainbow')
