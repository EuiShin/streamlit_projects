# streamlit run c:/Users/sui94/streamlit_study/font_color_choice.py
import streamlit as st
import numpy as np
import pandas as pd
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b]

def rgb_to_hex(colors):
    return f'#{colors[0]:02X}{colors[1]:02X}{colors[2]:02X}'

def hex_to_rgb(hex_color):
    """'#RRGGBB' 형식의 문자열을 [R, G, B] 리스트로 변환"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return [0, 0, 0]
    return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

# 인공신경망 학습용
def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

@st.cache_resource
def neural_network(inputs, outputs):
    n_hidden_1=10
    n_hidden_2=5
    epochs=10000
    lr=0.1
    
    np.random.seed(1)
    weights_input_hidden1 = np.random.rand(3, n_hidden_1)
    weights_hidden1_hidden2 = np.random.rand(n_hidden_1, n_hidden_2)
    weights_hidden2_output = np.random.rand(n_hidden_2, 1)

    for _ in range(epochs):
        # 순전파
        h1_input = np.dot(inputs, weights_input_hidden1)
        h1_output = sigmoid(h1_input)
        
        h2_input = np.dot(h1_output, weights_hidden1_hidden2)
        h2_output = sigmoid(h2_input)


        final_input = np.dot(h2_output, weights_hidden2_output)
        final_output = sigmoid(final_input)

        # 오차 계산
        error = outputs - final_output

        # 역전파
        d_output = error * sigmoid_derivative(final_output)
        d_hidden2 = d_output.dot(weights_hidden2_output.T) * sigmoid_derivative(h2_output)
        d_hidden1 = d_hidden2.dot(weights_hidden1_hidden2.T) * sigmoid_derivative(h1_output)

        # 가중치 업데이트
        weights_hidden2_output += h2_output.T.dot(d_output) * lr
        weights_hidden1_hidden2 += h1_output.T.dot(d_hidden2) * lr
        weights_input_hidden1 += inputs.T.dot(d_hidden1) * lr

    return weights_hidden2_output, weights_hidden1_hidden2, weights_input_hidden1

def predict_color(rgb, w_ih1, w_h1h2, w_h2o):
    hidden1 = sigmoid(np.dot(rgb, w_ih1))
    hidden2 = sigmoid(np.dot(hidden1, w_h1h2))
    output = sigmoid(np.dot(hidden2, w_h2o))
    return output

if "x" not in st.session_state:
    st.session_state.x = []

if "y" not in st.session_state:
    st.session_state.y = []

if "n" not in st.session_state:
    st.session_state.n = 0

if "weight" not in st.session_state:
    st.session_state.weight = []

st.title('🧠 글씨 색상 추천기')
st.write('''
    배경색을 보고 어울리는 글씨 색을 선택해 주세요 (검정/흰색)   
    선택한 글씨 색 데이터를 활용하여 배경색에 어울리는 폰트의 색상(검/흰)을 예측합니다.
''')



background_color_rgb = random_color()
background_color_hx = rgb_to_hex(background_color_rgb)

with st.container(border=True):

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div style="border:1px solid #ccc; padding: 20px; background-color:{background_color_hx}; color: black; text-align: center; font-size: 2em; font-weight: bold;">
                검은색
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("검은색 선택", use_container_width=True):
            st.session_state.x.append(background_color_rgb)
            st.session_state.y.append([1])
            st.session_state.n += 1

    with col2:
        st.markdown(
            f"""
            <div style="border:1px solid #ccc; padding: 20px; background-color:{background_color_hx}; color: white; text-align: center; font-size: 2em; font-weight: bold;">
                흰색
            </div>
            """,
            unsafe_allow_html=True   
        )
        if st.button("흰색 선택", use_container_width=True):
            st.session_state.x.append(background_color_rgb)
            st.session_state.y.append([0])
            st.session_state.n += 1


    col1, col2 = st.columns(2)
    with col1:
        st.write(f'현재까지 학습된 샘플 수: {st.session_state.n}')

    with col2:
        if st.button("🔄 데이터 초기화"):
            st.session_state.x = []
            st.session_state.y = []
            st.session_state.n = 0
            st.session_state.weight = []
            st.rerun()



if st.session_state.n >= 10:
    if st.button('✅ 학습 시작'):
        outputs = np.array(st.session_state.y)
        inputs = np.array(st.session_state.x) / 255

        weights_hidden2_output, weights_hidden1_hidden2, weights_input_hidden1 = neural_network(inputs, outputs)
        st.session_state.weight = [weights_hidden2_output, weights_hidden1_hidden2, weights_input_hidden1]
        st.success('✅ 학습 완료')

if st.session_state.weight != []:
    st.session_state.test_color = st.color_picker("예측할 색상을 선택하세요")
    test_rgb = hex_to_rgb(st.session_state.test_color)
    prediction = predict_color((np.array(test_rgb)/100).reshape(1, -1), st.session_state.weight[2], st.session_state.weight[1], st.session_state.weight[0])       
    st.write(f"예측 결과: {'검은색' if prediction[0][0] > 0.5 else '흰색'} (확률: {prediction[0][0]:.2f})")
    st.markdown(
        f"""
        <div style="border:1px solid #ccc; padding: 20px; background-color:{st.session_state.test_color}; color:{'black' if prediction[0][0] > 0.5 else 'white'}; text-align: center; font-size: 2em; font-weight: bold;">
            <h4>예측된 색상 미리보기</h4>
        </div>
        """, unsafe_allow_html=True
    )
    st.dataframe(st.session_state.weight[2])
    st.dataframe(st.session_state.weight[1])
    st.dataframe(st.session_state.weight[0])


st.write(' ')
