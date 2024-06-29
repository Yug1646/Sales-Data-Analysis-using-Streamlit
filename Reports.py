import File_Handling as fh
import streamlit as st
import matplotlib.pyplot as plt
import Analysis as an

df = fh.load_file()

st.title("Reports")

color_choice = st.color_picker("Pick A Color", "#00f900")

def bar_ch():
    h_v = an.head_graph()
    st.write('\n\n\n\n\n')
    st.subheader("Sales by Category")
    head_data = df.head(h_v)
    # st.bar_chart(df.head(h_v), y="Sales", color=color_choice,horizontal=True)
    st.bar_chart(head_data.set_index('Category')['Sales'], use_container_width=True, color=color_choice)
bar_ch()

def line_ch():
    st.subheader("Line Chart")
    line = df.groupby("Category")["Profit"].count()
    st.line_chart(line.head(10),color=color_choice)
    
line_ch()

def pie_ch():
    sub_category_count = df['Category'].value_counts().head(10)
    st.subheader("Pie Chart")
    fig, ax = plt.subplots(figsize=[10, 10])
    fig.patch.set_alpha(0)
    ax.pie(sub_category_count.values, autopct='%1.1f%%', labels=sub_category_count.index,textprops={'color': 'white'})
    st.pyplot(plt)

pie_ch()
