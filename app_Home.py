from inspect import isframe
import streamlit as st

def run_home_app():
    st.text('안녕하세요. 환영합니다')
    st.text('이 앱은 대한민국 공직자들의 공무원 연금 가입에 대한 통계 앱입니다.') 
    #img_url = 'https://image.lawtimes.co.kr/images/55555(4).jpg'
    #st.image(img_url)
    #video_file = 'https://www.youtube.com/embed/OA-GpBpJEGA' embed => v 로 수정함
    #video_file = 'https://www.youtube.com/v/OA-GpBpJEGA?version=2&autoplay=1'
    #st.video(video_file,start_time=0)
    st.video("https://youtu.be/OA-GpBpJEGA?t=19")
if  __name__=='__main__':
    main()     