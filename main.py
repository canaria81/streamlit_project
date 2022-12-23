from tkinter import Menu
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
from dateutil.parser import parse
from datetime import date

from app_Home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main():
   st.title('공무원연금 가입자 주요 통계 앱')
   menu = ['Home', '데이터 분석', '예측']
   choice = st.sidebar.selectbox('메뉴', menu)
   img_url = 'https://image.lawtimes.co.kr/images/55555(4).jpg'
   st.image(img_url)
   if choice == 'Home':
       run_home_app()
   elif choice == '데이터 분석' :
        run_eda_app()
   elif choice == '예측' :
        run_ml_app()  
if  __name__=='__main__':
    main()   