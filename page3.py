import streamlit as st

with st.sidebar:
    text=st.text_input("請輪入文字")
    st.write(f"你是一個{text}")

tab1,tab2,tab3=st.tabs(["A","B","C"])

with tab1:
    gender=st.radio("請問你是性別是",["男","女","跨性別"],index=None)
    if gender:
        st.write(f"你所選的性別是{gender}")

with tab2:
    contact=st.selectbox("您想要用什麼方式聯絡",["mail","tel","wechat","line","teams"],index=3)

    if contact:
        st.write(f"你所選的聯絡方式是{contact}")

with tab3:

    fruits=st.multiselect("您想吃什麼水果",["apple","banana","car","dog","eye","fire","water","watermelon"])

    for fruit in fruits:
        st.write(f"你所選的水果是{fruit}")

with st.expander("身高height"):

    height=st.slider("你的身高是多少厘米",value=170,min_value=100,max_value=250,step=10)

    st.write(f"你的身體是{height}cm")

st.divider()

file=st.file_uploader("上傳文件",type=["pdf","jpg","png","jpeg","txt"])

if file:

    st.write(f"你所選的內容是{file.name}")

    st.divider()

    st.write(f"你選的內容是{file.read().decode("utf-8")}")
