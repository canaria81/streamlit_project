import streamlit as st
import numpy as np
import joblib
def run_ml_app():
    st.subheader('지역별 공무원 연금가입 예측건 수')
    gender = st.radio('성별 선택', ['여자', '남자'])
    if st.button('데이터프레임 보기'):
        st.dataframe(df)

    if gender == '여자' :
        gender = 0
    else :
        gender = 1
    age = st.number_input('나이 입력', 18, 100)

    salary = st.number_input('연봉 입력', 10000, 1000000)

    debt = st.number_input('카드빚 입력', 0, 1000000)

    worth = st.number_input('자산 입력', 1000, 10000000)

    new_data = np.array([gender, age, salary, debt, worth])

    print(new_data)

    new_data = new_data.reshape(1, 5)

    regressor = joblib.load('regressor.pkl')

    y_pred = regressor.predict(new_data)

    y_pred = round(y_pred[0] , 1)

    if y_pred < 0 :
        st.info('입력한 데이터로는 금액을 예측하기 어렵습니다.')    
    else :
        st.info('지역별 공무원 연금가입은 {}달러 입니다.'.format(y_pred))