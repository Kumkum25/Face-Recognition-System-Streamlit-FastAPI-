import streamlit as st
import requests
import cv2
import numpy as np
from PIL import Image
import os

# ================= CONFIG =================
DETECT_API = "http://127.0.0.1:8000/detect"
RECOGNIZE_API = "http://127.0.0.1:8000/recognize"
ADD_IDENTITY_API = "http://127.0.0.1:8000/add-identity"

GALLERY_DIR = "app/data/gallery"

st.set_page_config(page_title="Face Recognition System", layout="wide")
st.title("🙂 Face Recognition System")

tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Face Detection",
    "🧠 Face Recognition",
    "➕ Add Identity",
    "📋 List Identities"
])

# ======================================================
# 1️⃣ FACE DETECTION
# ======================================================
with tab1:
    st.subheader("Face Detection (Upload Image)")
    file = st.file_uploader("Upload image", ["jpg", "png", "jpeg"], key="detect")

    if file:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Input Image", width=350)

        if st.button("Detect Faces"):
            res = requests.post(DETECT_API, files={"file": file.getvalue()})

            if res.status_code == 200:
                img_np = np.array(img)
                img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

                for f in res.json()["faces"]:
                    x1, y1, x2, y2 = map(int, f["bbox"])
                    cv2.rectangle(img_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)

                st.image(
                    cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB),
                    caption="Detected Faces",
                    width=350
                )
            else:
                st.error(res.text)

# ======================================================
# 2️⃣ FACE RECOGNITION
# ======================================================
with tab2:
    mode = st.radio("Choose input method", ["Upload Image", "Camera Capture"])

    def draw_label(img, x1, y1, name, conf):
        label = f"{name} ({conf:.2f}%)"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1.0
        thickness = 3

        (tw, th), _ = cv2.getTextSize(label, font, font_scale, thickness)

        cv2.rectangle(
            img,
            (x1, y1 - th - 15),
            (x1 + tw + 10, y1),
            (0, 255, 0),
            -1
        )

        cv2.putText(
            img,
            label,
            (x1 + 5, y1 - 5),
            font,
            font_scale,
            (0, 0, 0),
            thickness,
            cv2.LINE_AA
        )

    if mode == "Upload Image":
        file = st.file_uploader("Upload image", ["jpg", "png", "jpeg"], key="rec_upload")

        if file:
            img = Image.open(file).convert("RGB")
            st.image(img, caption="Input Image", width=350)

            if st.button("Recognize"):
                res = requests.post(RECOGNIZE_API, files={"file": file.getvalue()})

                if res.status_code == 200:
                    data = res.json()
                    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

                    for r in data["results"]:
                        x1, y1, x2, y2 = map(int, r["bbox"])
                        cv2.rectangle(img_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)

                        for (x, y) in r["landmarks"]:
                            cv2.circle(img_bgr, (int(x), int(y)), 2, (0, 255, 255), -1)

                        draw_label(img_bgr, x1, y1, r["name"], r["confidence"])

                    st.image(
                        cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB),
                        caption="Recognition Result",
                        width=350
                    )
                else:
                    st.error(res.text)

    else:
        cam = st.camera_input("Capture image from camera")

        if cam:
            img = Image.open(cam).convert("RGB")
            st.image(img, caption="Captured Image", width=350)

            if st.button("Recognize Face"):
                res = requests.post(RECOGNIZE_API, files={"file": cam.getvalue()})

                if res.status_code == 200:
                    data = res.json()
                    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

                    for r in data["results"]:
                        x1, y1, x2, y2 = map(int, r["bbox"])
                        cv2.rectangle(img_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)

                        for (x, y) in r["landmarks"]:
                            cv2.circle(img_bgr, (int(x), int(y)), 2, (0, 255, 255), -1)

                        draw_label(img_bgr, x1, y1, r["name"], r["confidence"])

                    st.image(
                        cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB),
                        caption="Recognition Result",
                        width=350
                    )
                else:
                    st.error(res.text)

# ======================================================
# 3️⃣ ADD IDENTITY
# ======================================================
with tab3:
    mode = st.radio("Add Identity Using", ["Upload Image", "Camera Capture"])
    name = st.text_input("Enter person name")

    if mode == "Upload Image":
        file = st.file_uploader("Upload face image", ["jpg", "png", "jpeg"])

        if file:
            st.image(file, caption="Input Image", width=300)

            if st.button("Save Identity"):
                res = requests.post(
                    ADD_IDENTITY_API,
                    files={"file": file.getvalue()},
                    data={"name": name}
                )

                if res.status_code == 200:
                    st.success("✅ Identity saved")
                else:
                    st.error(res.text)

    else:
        cam = st.camera_input("Capture face image")

        if cam:
            st.image(cam, caption="Captured Image", width=300)

            if st.button("Save Identity"):
                res = requests.post(
                    ADD_IDENTITY_API,
                    files={"file": cam.getvalue()},
                    data={"name": name}
                )

                if res.status_code == 200:
                    st.success("✅ Identity saved")
                else:
                    st.error(res.text)

# ======================================================
# 4️⃣ LIST IDENTITIES
# ======================================================
with tab4:
    st.subheader("Registered Identities")

    if os.path.exists(GALLERY_DIR):
        for person in os.listdir(GALLERY_DIR):
            col1, col2 = st.columns([1, 4])
            img_path = os.path.join(GALLERY_DIR, person, "reference.jpg")

            with col1:
                if os.path.exists(img_path):
                    st.image(img_path, width=80)

            with col2:
                st.markdown(f"**{person}**")
    else:
        st.info("No identities found")
