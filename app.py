import streamlit as st
import pandas as pd
from analysis.insights import *

st.write("<h1 style=\"margin-bottom:70px;border-bottom:1px solid red\">My Finances</h1>",unsafe_allow_html=True)

navbar = st.sidebar.radio("Index",["Summary","Transactions","Graphs"])

if navbar=="Summary":
    c,d = summary()
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"<h3>CREDIT &nbsp&nbsp<span style=\"color:#67AE45;padding-left:30px\">₹{c}</span></h3>",unsafe_allow_html=True)
        st.write(f"<h3>DEBIT <span style=\"color:#CA6B6B;padding-left:60px\">₹{d}</span></h3>",unsafe_allow_html=True)
    with col2: 
        month,year = present_date()
        st.write(f"<h3 style=\"text-align:right\">{month.upper()} {year}</h3>",unsafe_allow_html=True)

    d,b = balance()
    st.write(f"<h3 style=\"border-top:1px solid red;margin-top:80px;padding-top:50px\">BALANCE <span style=\"color:yellow;padding-left:20px;\">₹{b}</span></h3>",unsafe_allow_html=True)

if navbar=="Transactions":
    st.dataframe(transactions_list())
