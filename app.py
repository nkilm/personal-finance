import streamlit as st
import pandas as pd
from analysis.insights import *

st.write("<h1 style=\"color:#fff;text-align:center;\">My Finances</h1>",unsafe_allow_html=True)

navbar = st.sidebar.radio("Index",["Summary","Transactions","Graphs"])

if navbar=="Summary":
    c,d = summary()
    st.write(f"<h3>CREDIT &nbsp&nbsp<span style=\"color:#67AE45\">₹{c}</span></h3>",unsafe_allow_html=True)
    st.write(f"<h3>DEBIT <span style=\"color:#CA6B6B;padding-left:30px\">₹{d}</span></h3>",unsafe_allow_html=True)

if navbar=="Transactions":
    st.dataframe(transactions_list())
