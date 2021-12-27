import streamlit as st
#text title
st.title('Streamlit Tutorials')

#Header/subheader
st.header('This is a header')
st.subheader('This is a subheader')

#text
st.text('Hello Streamlit')

#Markdown
st.markdown('')

#error/Colorful Text
st.success('Sucessful')
st.info('Information')
st.warning('This is a warning')
st.error('this is an error')
st.exception("NameError('name three not defined')")
st.



#get help info about python
st.help(range)

#writing Text
st.write('Text with title')
st.write(range(10))

#Images



from PIL import Image
img=Image.open('image.jpg')
st.image(img,width=300,caption='Simple Image')

#videos
vid_file=open(cartoonvideo.html,).read()
st.video(vid_file)

audio_file=


