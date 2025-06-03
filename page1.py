import streamlit as st
import pandas as pd

st.title("歐盈吟是大美女😊😎💖🎶")

st.write("### 我愛您!!!!!!")

[11,22,33]

{"a":"1","b":"2","c":"3","d":"4"}


st.image(r"C:\Users\DELL\Downloads\Synthetic Rubbers_KIBIPOL PR-040Gs_600.jpg",width=100)
st.image(r"C:\Users\DELL\Downloads\Synthetic Rubbers_KIBIPOL PR-040Gs_600.jpg",width=200)
st.image(r"C:\Users\DELL\Downloads\Synthetic Rubbers_KIBIPOL PR-040Gs_600.jpg",width=400)
st.image(r"C:\Users\DELL\Downloads\Synthetic Rubbers_KIBIPOL PR-040Gs_600.jpg",width=800)
st.image(r"C:\Users\DELL\Downloads\Synthetic Rubbers_KIBIPOL PR-040Gs_600.jpg",width=1000)


df=pd.DataFrame({"學校":["A","B","C","D"],"班級":["甲","乙","丙","丁"],"學號":[1,2,3,4]})

st.dataframe(df)

st.divider()

st.table(df)

st.divider()

st.radio("您的性別是",["男","女","跨性別"],index=1)

