# streamlit run c:/Users/sui94/streamlit_study/app.py
import streamlit as st

def dict_to_badge(dict):
    badge_str = ''
    for key, value in dict.items():
        badge_str += f':{value}-badge[{key}]  '
    return badge_str


st.write('# 안녕하세요 신의 입니다')
st.write('''
    데이터분석가 신의 입니다.   
    데이터와 기술을 통해 비즈니스 문제를 해결합니다.
''')

st.header("Skills", divider=True)
skills_1 = {
    'python' : 'blue',
    'SQL' : 'red', 
    '데이터시각화' : 'green',
    'Redash' : 'red',
    'GoogleSheets' : 'orange',
    '사업기획' : 'violet',
    '모바일분석' : 'blue',
    '머신러닝' : 'blue', 
    '통계분석' : 'blue',
    '유저분석' : 'blue',
    '통계분석' : 'blue',
    '마케팅분석' : 'blue',
    'AARRR' : 'green',
    'Cohort' : 'green', 
    'Retention' : 'green',
    'A/B테스트' : 'green',
    'GoogleAnalytics' : 'violet',
    'Braze' : 'violet', 
    'Salesforce' : 'violet',
    'Zapier' : 'violet',
}

st.markdown(dict_to_badge(skills_1))

st.header("경력", divider='rainbow')

st.header("학업", divider='rainbow')

