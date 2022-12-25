from inspect import isframe
import streamlit as st

def run_home_app():
    img_url = 'https://image.lawtimes.co.kr/images/55555(4).jpg'
    st.image(img_url)
    st.text('안녕하세요.')
    st.text('이 앱은 대한민국 공직자들의 공무원 연금 가입에 관련한 통계 입니다.') 
    #video_file = 'https://www.youtube.com/embed/OA-GpBpJEGA' embed => v 로 수정함
    #video_file = 'https://www.youtube.com/v/OA-GpBpJEGA''
    #st.video("https://youtu.be/OA-GpBpJEGA?t=5")
    st.video('https://youtu.be/Dz6C-QkliQE?list=PLVcXm3IuSymgxoIUKdw1qSwOlL-b7tJnY&t=19')
    
if  __name__=='__main__':
    main()     