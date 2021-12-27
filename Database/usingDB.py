import streamlit as st 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Smartphone
engine= create_engine("sqlite:///mydatabase.sqlite")

makeSession=sessionmaker(bind=engine)
sess= makeSession()

st.title('Add New  SmartPhone Data')
st.markdown('---')
brand_v=st.text_input('Brand')
rom_v=st.text_input('Internal Storage')
ram_v=st.text_input('RAM')
camera_v=st.text_input('camera')

st.markdown("""
#
""")
btn=st.button("Add Button")

if btn:
    smrtphn = Smartphone(brand=brand_v, rom=rom_v,ram=ram_v,Camera=camera_v)
    sess.add(smrtphn)
    sess.commit()

    st.success('Data saved')
