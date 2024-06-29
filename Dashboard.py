# This file is used to call the function made in Analysis.py 
import streamlit as st
import Analysis as an

st.title('Dashboard')
st.markdown("---")


cust_count = st.radio(
    "Select the Country",
    ["CA", "US"],
    index=0)

an.count_customer(cust_count)

an.avg_itemorder()

an.min_itemorder()

an.max_itemorder()

an.sort_data()

st.subheader("Top Visited Customer(s):")
head_cust=an.head_graph()
an.repeat_customer(head_cust)