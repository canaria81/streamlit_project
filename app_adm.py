import streamlit as st
import pandas as pd
import numpy as np
def run_adm_app():
    df = pd.read_csv('data/공무원연금공단_공무원연금주요통계(지역별 가입자 추이)_20211231.csv', encoding='MS949')
    st.info('관리자만 가능한 화면입니다.')
    password = st.text_input('패스워드를 입력하세요.', type='password')
    if password:
        if password == 'admin':
            st.dataframe(df)
            st.write(f'현재 데이터는 {df.shape[0]}행  {df.shape[1]}열')
            #st.write('')           
            st.subheader('업데이트 데이터 추가')
            file = st.file_uploader('CSV 파일 업로드', type=['csv'])
            if file is not None:
                df_new = pd.read_csv(file) 
                st.dataframe(df_new)
                st.warning('기존 데이터프레임에 추가하고 파일을 저장하시겠습니까?')
                admin_choice =st.text_input("저장")
                if admin_choice:
                    if admin_choice =='저장':
                       df.to_csv('공무원연금공단_공무원연금주요통계(지역별 가입자 추이)_20211231.csv')
                    st.success('저장에 성공했습니다.')
                    st.dataframe(df)
                    st.write(f'현재 데이터는 {df.shape[0]}행  {df.shape[1]}열')
                else:
                    st.error('파일 확장자를 확인.')                                     
            else:
               st.info('작업을 취소.')                              
        else:
            st.error('패스워드가 틀렸어요. 패스워드 입력 요청.')