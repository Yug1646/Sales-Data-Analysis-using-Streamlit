import streamlit as st

st.title('Introduction')
st.markdown('---')
# st.subheader(divider='gray')
intro="""In this era,development of a successfull business depends on the customer's behaviour. A great customer experience can be a reason for company's growth
To implement that we have analyzed Sales data also considering customer's point of view.Sales data analysis involves examining various metrics and trends to derive actionable insights that can enhance the overall performance of the store."""
st.write(intro)

st.header('Key objectives of Sales data analysis')

# Key objectives of Sales data analysis
st.markdown('---')
key_points = """\n1. Understanding customer's behaviour
   \n - Firstly, we gathered the data and to understand the data we have displayed the dataset in Cleaned Dataset page
\n2. Having a clean data
    \n - A clean data is a must to perform accurate analysis on it. We have cleaned data on Cleaned Dataset
\n3. Exploring Data Analysis(EDA)
    \n - We used statistical and graphical methods to explore and summarize the data
\n4. Visualization and Reporting
    \n - Create dashboards and reports to present the findings in an understandable and actionable format."""
st.markdown(key_points)

st.markdown('---')

st.header('Conclusion')
st.markdown('---')
con = """By leveraging data-driven insights, businesses can make informed decisions, optimize their operations, and ultimately enhance their profitability and customer satisfaction. 
Embracing the power of data analytics will ensure that your website remains agile, responsive, and ahead of the curve in meeting the ever-evolving needs of your customers"""
st.markdown(con)