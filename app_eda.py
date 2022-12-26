import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# 이코드는 ec2에 한글 폰트가 설치되어 있어야 하고,fonc에서 한글 사용가능 하도록 셋팅
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_eda_app() :    
    df = pd.read_csv('data/공무원연금공단_공무원연금주요통계(지역별 가입자 추이)_20211231.csv', encoding='MS949')
    st.subheader('전체 데이터프레임_가입건 수  (최근연도 순)')
    check = st.checkbox('데이터 보기/숨기기', value=True)
    if check:
        st.dataframe(df.sort_values('구분',ascending= False))
        st.write(f'전체 데이터  :  {df.shape[0]}행,  {df.shape[1]}열 ')
    st.subheader('인천에서 연금 가입이 가장 많은 연도 순')
    st.dataframe( df.sort_values('인천',ascending= False))
    st.subheader('인천에서 연금 가입이 가장 적은 3개 연도')
    st.dataframe(df.head(3))
    st.subheader('기본 통계 데이터')
    st.dataframe( df.describe() )

    st.subheader('최대, 최소 데이터 확인')
    column_list = df.columns[1:]
    seleced_column = st.selectbox('조회 할 지역의 컬럼을 선택하세요.', column_list)

    df_max = df.loc[ df[seleced_column] ==  df[seleced_column].max() , ]
    df_min = df.loc[ df[seleced_column] ==  df[seleced_column].min() , ]

    st.text('선택한 지역의 공무원 연금 가입을 많이 한 연도의 데이터')
    st.dataframe(df_max)
    st.text('선택한 지역의 공무원 연금 가입을 적게 한 연도의 데이터')
    st.dataframe(df_min)
    st.subheader('각 컬럼의 히스토그램')

    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', column_list)
    my_bins = st.number_input('빈의 개수를 입력하세요', 5, 20, value=10, step=1)

    fig1 = plt.figure()
    plt.hist(data= df, x=histogram_column, rwidth=0.8, bins=my_bins)
    plt.title(histogram_column + 'Histogram')
    plt.xlabel(histogram_column)
    plt.ylabel('Count')
    st.pyplot(fig1)
    st.subheader('상관 관계 분석')
    selected_list = st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', column_list)
    if len(selected_list) >= 2 :
        df_corr = df[ selected_list ].corr()
        fig2 = plt.figure()
        sb.heatmap(data= df_corr, annot=True, fmt='.1f', cmap='coolwarm',
            vmin= -1, vmax= 1 , linewidths=0.5 )
        st.pyplot(fig2)