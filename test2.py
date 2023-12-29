import streamlit as st
import PIL as Image
from ultralytics import YOLO

tab_1, tab_2 = st.tabs(['about me', 'main page'])
with tab_1:
    st.title("about me")
with tab_2:
    st.title("main page")
    @st.cache_resource
    def load_model():
        mod = YOLO("/Users/shauryaseam/IdeaProjects/yolo/venv/yolov8s-cls.pt")
        return mod

    img = st.file_uploader('Select the image', type=['jpg','png','jpeg'])
    if img is not None:
        img = Image.open(img)
        st.markdown('Image Visualization')
        st.image(img)
        st.header('Melanoma Form Classification')
        model = load_model()
        res = model.predict(img)
        label = res[0].probs.top5
        conf = res[0].probs.top5conf
        conf = conf.tolist()
        col1,col2 = st.columns(2)
        col1.subheader(res[0].names[label[0]].title() +' with '+ str(conf[0])+' Confidence')
        col2.subheader(res[0].names[label[1]].title() +' with '+ str(conf[1])+' Confidence')