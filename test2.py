import streamlit as st
from PIL import Image
from ultralytics import YOLO
import time

# Set page configuration
st.set_page_config(page_title="Moth-type Website", page_icon="🌞", layout="wide")

# Add a background color
st.markdown(
    """
    <style>
        body {
            font-family: 'Brush Script MT', cursive, sans-serif;
        }
        .stApp {
            background-color: #594773;
        }
        .stTabs {
            text-align: center;
        }
        .stTab {
            display: inline-block;
            justify-align: center;
        }
        .stTabLabel {
            justify-content: center;
        }
        .stTitle {
            text-align: center;
            font-family: 'Brush Script MT', cursive, sans-serif;
            font-size: 3em;
        }
        .toggle-center {
            display: flex;
            justify-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='stTitle'>MOTH CLASSIFICATION WEBSITE</h1>", unsafe_allow_html=True)
dark_mode = st.toggle("Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #0a1813; 
                color: #ffffff;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #594773; 
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

tab_1, tab_2, tab_3 = st.tabs(['Main Page', 'About Me', 'Feedback'])
with tab_1:
    st.title("Main Page")
    st.divider()
    st.write(
        "Welcome to the Moth-type Detection App, your go-to destination for effortlessly identifying moth species with cutting-edge technology! Our application leverages the power of YOLO (You Only Look Once), a state-of-the-art object detection algorithm, to provide you with swift and accurate predictions on the species of moths depicted in your images. Gone are the days of uncertainty when encountering a mysterious moth fluttering by. With our user-friendly interface, all you need to do is upload an image, and let the magic unfold before your eyes. Our advanced system processes the image in real-time, swiftly analyzing its contents and generating precise predictions regarding the moth species present. Whether you're a seasoned lepidopterist, a curious nature enthusiast, or simply someone intrigued by the wonders of the insect world, our Moth-type Detection App is designed to cater to your needs. Discover the fascinating diversity of moth species with just a click, as our intuitive platform seamlessly combines technology and nature exploration."
    )
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.header("21 Most Incredible Moth Species")
        st.write("Check out some of the most fascinating moth species!")
        st.video("https://www.youtube.com/watch?v=YaI1zE3AOXo")
        st.caption("Credit: https://www.youtube.com/@EpicWildlife")
        st.divider()
        st.header("21 Most Incredible Moth Species")
        st.write("Learn about the various types of moth species!")
        st.video("https://www.youtube.com/watch?v=qoyC1iejX08")
        st.caption("Credit: https://www.youtube.com/@Balyanak")


    with col2:
        st.subheader("Upload Image for classification below!")
        @st.cache_resource
        def load_model():
            mod = YOLO("/Users/shauryaseam/IdeaProjects/yolo/venv/yolov8s-cls.pt")
            return mod

        img = st.file_uploader('Select the image', type=['jpg','png','jpeg'])
        if img is not None:
            img = Image.open(img)
            st.markdown('Image Visualization')
            st.image(img)

            # Perform YOLO predictions
            st.subheader("Results:")
            progress_text = "Prediction in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            # Simulate predictions (replace with actual YOLO prediction logic)
            model = load_model()
            res = model.predict(img)
            label = res[0].probs.top5
            conf = res[0].probs.top5conf
            conf = conf.tolist()
            col1, col2 = st.columns(2)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            col1.subheader('#1) '+res[0].names[label[0]].title() + ' with ' + str(int(conf[0]*100)) + '% Confidence')
            col2.subheader('#2) '+res[0].names[label[1]].title() + ' with ' + str(int(conf[1]*100)) + '% Confidence')
            st.balloons()
            time.sleep(1)
            my_bar.empty()


with tab_2:
    st.title("About Me")
    st.divider()
    st.header("HELLO!")
    st.subheader("My name is Shaurya Seam...")

with tab_3:
    st.title("Feedback")
    st.divider()

    with st.form("Feedback Form"):
        # Add form components
        name = st.text_input("Name")
        email = st.text_input("Email")
        rating = st.slider("Rating (out of 10)", min_value=0, max_value=10, value=5)
        feedback_text = st.text_area("Feedback")

        # Add a submit button
        submit_button = st.form_submit_button("Submit Feedback")

    # Handle form submission
    if submit_button:
        # Process the feedback data (you can add your logic here)
        st.success(f"Feedback submitted: Name: {name}, Email: {email}, Rating: {rating}, Feedback: {feedback_text}")
