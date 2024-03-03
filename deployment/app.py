# import libraries 
import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_webrtc import webrtc_streamer
from turn import get_ice_servers
import mediapipe as mp
import numpy as np
import pickle
import cv2
import av
import os


# create objects just focus on the hands 
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# get the model that detect hand_landmarks 
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# load model
model_file = open('model.pickle','rb')
model_dict = pickle.load(model_file)
model = model_dict['model']

# define convertor from index number to the equivelant label as dictionary
index_to_label = {0:'Goodbye', 1:'Hello', 2:'Help', 3:'Sorry', 4:'Thankyou'}


def video_processing(frame):

    frame = frame.to_ndarray(format="bgr24")
    
    # flipping the frame horizontally
    frame = cv2.flip(frame, 1)

    # convert frame to rgb
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # get hands detection on the rgb image 
    result = hands.process(frame_rgb)
    
    # define lists
    current_image_landmarks = []
    all_landmarks = []
    
    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            # draw the landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmark, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
                
            for landmark in hand_landmark.landmark:
                current_image_landmarks.append(landmark.x)
                current_image_landmarks.append(landmark.y)

        # check that the number of landmarks are equal for each image
        if len(current_image_landmarks) < 84:
            current_image_landmarks = current_image_landmarks + [0]*(84-len(current_image_landmarks))

        # append the value of current_image_data in the all_data list
        all_landmarks.append(current_image_landmarks)
        
        # convert the all_landmarks from list to 2d array
        all_landmarks_array = np.array(all_landmarks)
        
        prediction = model.predict(all_landmarks_array)[0]
        prediction_with_probability = max(model.predict_proba(all_landmarks_array)[0])

        # prepare the text
        class_label = index_to_label[prediction]
        full_text = f'{class_label}, {prediction_with_probability}'

        # Write it on the frame
        cv2.putText(frame, full_text, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,0,255), 3, cv2.LINE_AA)
    
    # convert it to bgr image
    return av.VideoFrame.from_ndarray(frame, format="bgr24")

##################################### Run #####################################################

with st.sidebar:
    selected  = option_menu(
        menu_title= 'Menu',
        options=['Home', 'App', 'Contact'],
        icons=['house-fill', 'terminal-fill', 'person-lines-fill']
    )

if selected == 'Home':
    # Title
    st.title('Home')
    st.markdown("Hello👋, I'm Mohamed Elsharkawy, a Data Science and AI enthusiast🥰. I recently completed a Sign Language Recognition project🧑‍💻, furthering my skills in computer vision. This project was a big step in my learning journey into AI, and I'm always seeking improvement through self-learning and making projects.⚒️")
    st.markdown("Thank you for taking the time to see about my project.❤️")
    st.markdown("""
## Used Technologies:

- :snake: **Python**: Programming language used for the project.
- :hourglass_flowing_sand: **Mediapipe**: Used for hand tracking and pose estimation.
- :1234: **NumPy**: Library for numerical computations in Python.
- :bar_chart: **Scikit-learn**: Machine learning library used for modeling.
- :camera: **OpenCV**: Computer vision library for image processing.
- :computer: **JupyterLab**: Interactive development environment for data science.
- :cloud: **Google Colab**: Cloud-based platform for running Jupyter notebooks.
- :pick: **Pickle**: Python module for object serialization.

 """)
    st.markdown('---')

    # Section 1 -> Demo for the project
    st.markdown('### Demo')
    st.image(os.path.join('Demo.gif'))
    st.markdown('---')


    # Section 2 --> Description about the 
    st.markdown('### Description')
    st.write(
        '''
            It is a sign language recognition project, used to ease the communication between normal people and deaf-mute individuals. 
            The project focuses on recognizing American Sign Language (ASL) hand gestures for the following signs: Goodbye, Hello, Help, Sorry, Thank you.
        '''
    ) 
    st.markdown('---')

    # Section 3 --> Clarify the used sign languages
    st.markdown('### Used ASL Signs')
    images = ['Goodbye', 'Hello', 'Help', 'Sorry', 'Thankyou']

    value = st.selectbox('Select a Sign :', images)
    placeholer = st.empty()

    if value == 'Goodbye':
        goodbye_path = os.path.join('Images', 'Goodbye.jpg')
        placeholer.image(goodbye_path, width=700)
    
    if value == 'Hello':
        hello_path = os.path.join('Images', 'Hello.jpg')
        placeholer.image(hello_path, width=700)

    if value == 'Help':
        help_path = os.path.join('Images', 'Help.jpg')
        placeholer.image(help_path, width=700)

    if value == 'Sorry':
        sorry_path = os.path.join('Images', 'Sorry.jpg')
        placeholer.image(sorry_path, width=700)

    if value == 'Thankyou':
        thankyou_path = os.path.join('Images', 'Thankyou.jpg')
        placeholer.image(thankyou_path, width=700)
    
    st.markdown('---')

    # Section 4 --> get the project 
    st.markdown('### Project Code')
    st.markdown('You Can Access The Whole Project [Here](https://github.com/mohamedelsharkawy-coder/Sign-Language-Recognition-with-Hand-Gestures/tree/main)')

if selected == 'App':
    st.title("Real Time ASL Recognition")
    webrtc_streamer(key='object_detection', video_frame_callback=video_processing, rtc_configuration={"iceServers": get_ice_servers()}, 
                    media_stream_constraints={"video": True, "audio": False})

if selected == 'Contact':
    st.title('How to Reach Me')
    st.markdown(""" 
        - **Email**: [mohamed.k.elsharkawy@gmail.com](mailto:mohamed.k.elsharkawy@gmail.com)
        - **Phone**: [(+20) 1004622244](tel:+201004622244)
        - **LinkedIn**: [Profile](https://www.linkedin.com/in/mohamed-elsharkawy-6184b41a7/)
        - **Github**: [Profile](https://github.com/mohamedelsharkawy-coder)
                """)
    st.markdown("""
    If you have any suggestions or feedback about the app, feel free to contact me📨. Your input is valuable, and I welcome any recommendations or ideas you may have.❤️

""")












