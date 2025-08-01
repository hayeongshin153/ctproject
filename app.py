import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 설정
st.set_page_config(layout='wide', page_title='컴퓨팅사고력 문제 by SHY')

# 상단 헤더 꾸미기
st.markdown("""
    <div style="background-color:#f0f8ff;padding:20px;border-radius:10px;margin-bottom:20px;">
        <h1 style="text-align:center;color:#1c3f95;">🧠 컴퓨팅사고력 문제 해결 웹앱 by SHY</h1>
        <p style="text-align:center; font-size:18px; color:gray;">컴퓨팅사고력 기반 문제해결 교육 활동</p>
    </div>
""", unsafe_allow_html=True)

# 좌우 컬럼 나누기
col1, col2 = st.columns((3, 1))

with col1:
    with st.expander('📌1. 누구에게 문서를 전해줘야 할까?'):
        if os.path.exists("image.png"):
            st.image("image.png", caption="문제 이미지", use_container_width=True)
        else:
            st.warning("image.png 파일을 찾을 수 없습니다.")

        if os.path.exists("new version(origin) copy.html"):
            with open("new version(origin) copy.html", "r", encoding="utf-8") as f:
                html = f.read()
            components.html(html, height=800, scrolling=True)
        else:
            st.error("new version(origin) copy.html 파일이 없습니다.")

    with st.expander('📌2. 오늘은 어디로 가야할까? 수업 장소를 찾아라!'):
        if os.path.exists("new version(origin) copy 3.html"):
            with open("new version(origin) copy 3.html", "r", encoding="utf-8") as f:
                html = f.read()
            components.html(html, height=800, scrolling=True)
        else:
            st.error("new version(origin) copy 3.html 파일이 없습니다.")

    with st.expander('📌3. 오늘은 어디로 가야할까? 수업 장소를 찾아라! (applied AI.ver)'):
        if os.path.exists("new version(origin) copy 2.html"):
            with open("new version(origin) copy 2.html", "r", encoding="utf-8") as f:
                html = f.read()
            components.html(html, height=800, scrolling=True)
        else:
            st.error("new version(origin) copy 2.html 파일이 없습니다.")

with col2:
    with st.expander('Tips for Problem 1'):
        st.info('💡 CT 사고력 기반 문제 해결 과정')
        if os.path.exists("diagram1.html"):
            with open("diagram1.html", "r", encoding="utf-8") as f:
                html = f.read()
            components.html(html, height=900, scrolling=True)
        else:
            st.warning("diagram1.html 파일을 찾을 수 없습니다.")

    with st.expander('Tips for Problem 2'):
        st.info('💡 CT 사고력 기반 문제 해결 과정')
        if os.path.exists("diagram2.html"):
            with open("diagram2.html", "r", encoding="utf-8") as f:
                html = f.read()
            components.html(html, height=900, scrolling=True)
        else:
            st.warning("diagram2.html 파일을 찾을 수 없습니다.")

    with st.expander("Tips for Problem 3"):
        st.info("💡 인공지능 처리 과정 시각화")
        if os.path.exists("diagram3.png"):
            st.image("diagram3.png", use_container_width=True)
        else:
            st.warning("diagram3.png 파일을 찾을 수 없습니다.")

# 하단 푸터
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:blue;">© copyright. all rights reserved by SHY</div>', unsafe_allow_html=True)
