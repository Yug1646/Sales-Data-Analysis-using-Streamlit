import File_Handling as fh
import streamlit as st
import pandas as pd

df = pd.DataFrame(fh.load_file())

def sort_data():
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
    st.subheader('Filters')

    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df_sorted = df.sort_values(by='Order Date')
    # fh.save_file(df_sorted)

    df['Year']= df['Order Date'].dt.year

    years = df['Year'].unique()
    select1 = st.multiselect('Select Order Year', years)
    data =df['Year'].isin(select1)
    new = df[data]
    st.write(new)
    # #Completed

def repeat_customer(head_cust):
    count= df['EmailID'].value_counts()
    if len(count) < head_cust:
        frequent_cust= count
    else:
        frequent_cust= count.head(head_cust)
        
    # st.subheader("Top Visited Customer(s):")
    for email, count in frequent_cust.items():
        st.write(f"{email}: {count} times purchased")
    # #Completed
    
def head_graph():
    number = st.number_input("Insert a number", value=0, placeholder="Type a number...")
    st.write("The current number is ",number)
    number = int(number)
    return number
    # #Completed

def count_customer(country):
    filtered_data = df[df['Order ID'].str.startswith(country)]   
    st.subheader('Count of Customer')
    count_value = filtered_data.shape[0]
    st.write(f'Count of customer from {country} : {count_value}')
    # Completed

def min_itemorder():
    min_index = df['Sales'].idxmin()
    min_name = df.loc[min_index]
    st.subheader('\n \n \n \nLeast Item Purchased')
    for key, value in min_name.items():
        st.write(f"{key}: {value}")
    # Completed

def max_itemorder():
    max_index = df['Sales'].idxmax()
    max_name = df.iloc[max_index]
    st.subheader('\n \n \n \nMost Item Purchased')
    for key, value in max_name.items():
        st.write(f"{key}: {value}")
    # Completed

def avg_itemorder():
    avg_sales = 0.0
    st.subheader('Average Sales')
    option = st.selectbox(
        "Select Category",
        df['Category'].unique(),  # Ensure unique categories
        index=None,
        placeholder="Select category"
    )

    if option:
        avg_sales = df[df['Category'] == option]['Sales'].mean()
        avg_sales = round(avg_sales, 2)
        st.write(f'Average Sales for {option}: {avg_sales}')
    else:
        st.write("Please select a category.")