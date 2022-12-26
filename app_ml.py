import streamlit as st
import numpy as np
import pandas as pd
# plotly 라이브러리 
import plotly.express as px
# altair 라이브러리
import altair as alt

def run_plotly_app():
    df = pd.read_csv('data/공무원연금공단_공무원연금주요통계(지역별 가입자 추이)_20211231.csv', encoding='MS949')
    st.subheader('전체 공무원 연금 가입건 수  (최근연도 순)')
    st.dataframe(df.sort_values('구분',ascending= False))
    st.write(f'전체 데이터  :  {df.shape[0]}행 {df.shape[1]}열 ')
    column_menu = df.columns[ 1 : ]
    choice_list = st.multiselect('지역을 선택하세요.', column_menu)
    if len(choice_list) != 0 :
        # 유저가 선택한 언어만, 차트를 그린다.
        df_selected = df[choice_list]
        ## 스트림릿에서 제공하는 라인차트 
        st.line_chart(df_selected)
        ## 스트림릿에서 제공하는 영역차트 
        st.area_chart(df_selected)
        ## 스트림릿에서 제공하는 바차트
        st.bar_chart(df_selected)
    df2 = pd.read_csv('data/공무원연금공단_공무원연금주요통계(지역별 가입자 추이)_20211231.csv', encoding='MS949')
    st.subheader('연금 가입건 수 데이터 5건 ')
    st.dataframe(df.head())
if __name__ == '__main__' :
    main()    