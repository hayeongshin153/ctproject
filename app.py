import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide', page_title='컴퓨팅사고력 문제 by SHY')
st.title('This is SHY Webapp!!')



col1, col2 = st.columns((3, 1))  # 예: 왼쪽이 75%, 오른쪽이 25%

with col1:
    with st.expander('누구에게 문서를 전해줘야할까?'):
        st.image("image.png", caption="문제 이미지", use_container_width=True)
        with open('./new version(origin) copy.html', 'r', encoding='utf-8') as f:
            html = f.read()
        components.html(html, height=800, scrolling=True)

    with st.expander('오늘은 어디로 가야할까? 수업 장소를 찾아라!'):
        with open('./new version(origin) copy 3.html', 'r', encoding='utf-8') as f:
            html = f.read()
        components.html(html, height=800, scrolling=True)

    with st.expander('오늘은 어디로 가야할까? 수업 장소를 찾아라!(AI.ver)...'):
        with open('./new version(origin) copy 2.html', 'r', encoding='utf-8') as f:
            html = f.read()
        components.html(html, height=800, scrolling=True)

with col2:
    with st.expander('Tips1..'):
        st.info('Tips for Problem 1')

        with open("diagram1.html", "r", encoding="utf-8") as f:
            html = f.read()
        components.html(html, height=900, scrolling=True)

    with st.expander('Tips2..'):
        st.info('Tips for Problem 2')

        with open("diagram2.html", "r", encoding="utf-8") as f:
            html = f.read()
        components.html(html, height=900, scrolling=True)

    with st.expander("Tips3.."):
        st.info("Tips for Problem 3")
        st.image("diagram3.png", use_container_width=True)



st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by SHY</font>', unsafe_allow_html=True)
