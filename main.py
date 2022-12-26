import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb

from dateutil.parser import parse
from datetime import date
import pandas as pd 
from PIL import Image

from app_Home import run_home_app
from app_adm import run_adm_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main():   
   st.title('공무원연금 관련 주요 통계 앱')
   img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHaxbuapl2vBrkFP3bugD8pyrLkWlew1pyYQ&usqp=CAU'
   st.sidebar.image(img_url,width=300)
   menu = ['Home','데이터 분석', '예측','Admin']
   choice = st.sidebar.selectbox('메뉴', menu)
   
   if choice == 'Home':
       run_home_app()
   elif choice == '데이터 분석' :
       run_eda_app()
   elif choice == '예측' :
       run_ml_app()     
   elif choice == 'Admin' :
       run_adm_app() 
if  __name__=='__main__':
    main()   