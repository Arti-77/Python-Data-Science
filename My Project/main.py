import streamlit as st
st.title('Customer Telegram Bot Using Python')
st.image('hero.jpg', use_column_width=True)
sidebar= st.sidebar
sidebar.title('User Options')
def introduction():
    st.markdown("""
        ## Heading Level2
        -Feature 1
        -Feature2
        -Feature3
    """)
    c1,c2=st.columns(2)
    c1.header('Column 1 Content')
    c2.header('column 2 Content')

def execute()
st.subheader('Project Working here')


options=['Project Introduction','Execution']

seloption=sidebar.selectbox('Select an Option',options)
if seloption==options[0]:
    introduction()
elif seloption==option[1]:
    execute()
