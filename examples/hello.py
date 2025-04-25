import streamlit as st

st.title('Hello Streamlit-er 한글')
st.markdown(
    '''
    This is a playground for you to try Streamlit and have fun.    
    여기는 스트림릿을 가지고 노는 놀이터야

    **There's :rainbow[so much] you can build!**
    **만들어 볼 수 있는 많은 것들이 있어**
    
    We prepared a few examples for you to get started. Just click on the buttons above and discover what you can do with Streamlit.     
    몇개의 예를 준비했어
    '''
)

if st.button('Send ballons!'):
    st.balloons()