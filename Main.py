import streamlit as st

pages = {
    "Home" : [
        st.Page("Home.py",title="Home Page",icon="🏠")
    ],
    "Cleaning" : [
        st.Page('Cleaning.py',title='Cleaned Dataset',icon="1️⃣")
    ],
    "Report" : [
        st.Page('Reports.py',title='Report of Data',icon="2️⃣")
    ],
    "Dashboard": [
        st.Page('Dashboard.py',title='Dashboard',icon="3️⃣")
    ]
}
pg = st.navigation(pages)
pg.run()