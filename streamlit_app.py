import tempfile

import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import time

model = YOLO("best (2).pt")
demo_img = "Team.jpeg"
DEMO_VIDEO = "1.mp4"

st.title('Face Detection Application')

st.markdown(
    """
    <style>
    [data-id="stSidebar"][aria-expanded="true"]> div:first-child{
        width:350px
    }
    [data-id="stSidebar"][aria-expanded="false"]> div:first-child{
        width:350px
        margin-left: -350px
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title("Faces")
st.sidebar.subheader('Parameters')


app_made = st.sidebar.selectbox('choose the app mode',
                                   ['About app','Run on image','Run on Video'])


if app_made == "About app":
    st.markdown('Coming soon')
    st.markdown(
    """
    <style>
    [data-id="stSidebar"][aria-expanded="true"]> div:first-child{
        width:350px
    }
    [data-id="stSidebar"][aria-expanded="false"]> div:first-child{
        width:350px
        margin-left: -350px
    }
    </style>
    """,
    unsafe_allow_html = True,
    )


elif app_made == "Run on image":

    st.markdown("**Detected Face**")
    kpi1_text = st.markdown(0)

    #========Upload image file===========#
    img_file_buffer = st.sidebar.file_uploader("Upload an Image",type=["jpg","jpeg","png"])

    #========Opened image file===========#
    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
    else:
        demo_images = demo_img
        image = Image.open(demo_images)
    st.sidebar.text('Orginal IMG')
    st.sidebar.image(image)

    #=========Detection============#
    results = model(image)
    counts = 0
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            if cls == 0:
                counts += 1
            else:
                counts = 1
    res = results[0].plot()
    out_image = res[:, :, ::-1]
    kpi1_text.write(f"<h1 style ='text-align: center; color:red;'>{counts}</h1>",unsafe_allow_html=True)
    st.subheader('Output Image')
    st.image(out_image, use_column_width=True)


elif app_made == "Run on Video":
    use_webcame  = st.sidebar.button('Use Webcame')
    record = st.sidebar.checkbox("Record Video")
    enable_GPU = st.sidebar.checkbox('Enable GPU')

    if record:
        st.checkbox("Recording",value=True)
    st.markdown(
        """
        <style>
        [data-id="stSidebar"][aria-expanded="true"]> div:first-child{
            width:350px
        }
        [data-id="stSidebar"][aria-expanded="false"]> div:first-child{
            width:350px
            margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('## Output')

    stframe = st.empty()
    video_file_buffer = st.sidebar.file_uploader("Upload a Video",type = ["mp4","movi","avi","m4v"])
    tffile = tempfile.NamedTemporaryFile(delete=False)

    if not video_file_buffer:
        if use_webcame:
            vid = cv2.VideoCapture(0)
        else:
            vid = cv2.VideoCapture(DEMO_VIDEO)
            tffile.name = DEMO_VIDEO
    else:
        tffile.write((video_file_buffer.read()))
        vid = cv2.VideoCapture(tffile.name)

    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    heigt = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_input = int(vid.get(cv2.CAP_PROP_FPS))

    codec = cv2.VideoWriter_fourcc('M','J','P','G')
    out = cv2.VideoWriter('output1.mp4',codec,fps_input,(width,heigt))

    st.sidebar.text('Input Video')
    st.sidebar.video(tffile.name)

    fps = 0
    i = 0

    kpi1,kpi2,kpi3 = st.columns(3)

    with kpi1:
        st.markdown("**Frame Rate**")
        kpi1_text = st.markdown("0")
    with kpi2:
        st.markdown("**Detected Faces**")
        kpi2_text = st.markdown("0")
    with kpi3:
        st.markdown("**Image Width**")
        kpi3_text = st.markdown("0")

    st.markdown("<hr/>",unsafe_allow_html = True)
    cap = cv2.VideoCapture(tffile.name)
    prevTime = 0
    while cap.isOpened():
        success,frame = cap.read()
        if success:
            results = model(frame)
            counts = 0
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls = int(box.cls[0])
                    if cls == 0:
                        counts += 1
                    else:
                        counts = 1
            res = results[0].plot()
            out_image = res[:, :, ::-1]
        currTime = time.time()
        fps=1/(currTime-prevTime)
        prevTime=currTime

        if record:
            out.write(frame)

        kpi1_text.write(f"<h1 style ='text-align: center; color:red;'>{int(fps)}</h1>", unsafe_allow_html=True)
        kpi2_text.write(f"<h1 style ='text-align: center; color:red;'>{counts}</h1>", unsafe_allow_html=True)
        kpi3_text.write(f"<h1 style ='text-align: center; color:red;'>{width}</h1>", unsafe_allow_html=True)

        frame = cv2.resize(frame,(0,0),fx = 0.8,fy = 0.8)
        stframe.image(out_image,channels = 'RGB',use_column_width = True)
    st.text('Video Processed')
    output_video = open('output1.mp4','rb')
    out_bytes = output_video.read()
    st.video(out_bytes)

    vid.release()
    out.release()
