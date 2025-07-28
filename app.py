import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout='wide', page_title='Time table!!!')

st.title('This is SHY Webapp!!')

with open('./new version(origin) copy 2.html', 'r', encoding='utf-8') as f:
    html = f.read()

col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)

    with st.expander('Content #2...'):
        components.html(html, height=800, scrolling=True)  

    with st.expander('Content #3...'):
        components.html(html, height=800, scrolling=True)  

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by SHY', unsafe_allow_html=True)
