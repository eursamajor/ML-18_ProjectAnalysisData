import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

data_day = pd.read_csv("day.csv")

st.markdown(
    "<h1 style='text-align: center;'>Bike Sharing Data Analysis</h1>",
    unsafe_allow_html=True
)

st.subheader('Penyewaan Sepeda per Bulan untuk Hari Kerja dan Hari Tidak Kerja')
col1, col2 = st.columns(2)

with col1:
    st.metric('Total Orders', value = '3,292,679')


with col2:
    st.markdown(
        """
        Member: 2,292,410 \n
        Pelanggan biasa: 1,000,269
    """)
st.image("penyewasepedabulanan.png")

st.subheader('Penyewaan Sepeda berdasarkan Musim dan Hari Kerja')
col3, col4 = st.columns(2)

with col3:
    st.metric('Total Orders', value = '3,292,679')


with col4:
    st.markdown(
    """
    <div style='margin-right: 100px;'>
        <p>Gugur: 918,583</p>
        <p>Panas: 1,061,129</p>
        <p>Semi: 841,613</p>
        <p>Salju: 471,348</p>
    </div>
    """,
    unsafe_allow_html=True)
st.image("berdasarkanmusim.png")