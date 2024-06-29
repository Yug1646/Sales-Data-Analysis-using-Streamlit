import File_Handling as fh
import streamlit as st

st.title('Cleaning Page')
st.markdown("---")

df = fh.load_file()

st.subheader('Cleaned Data')
st.write('1. Sorted Date')
st.write('2. Duplicates Removed')

st.write(df)
st.write(df.shape)

def convert_df(df):
    return df.to_csv().encode("utf-8")
csv = convert_df(df)

st.download_button(
    label="Download data",
    data=csv,
    file_name="Cleaned_Data.csv",
    mime="text/csv",
)