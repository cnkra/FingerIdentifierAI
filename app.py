import streamlit as st
import cv2
import mediapipe as mp
import pandas as pd
import os

# CSV setup
csv_path = "finger_data.csv"
columns = ['label'] + [f"{i}_{axis}" for i in range(21) for axis in ['x', 'y', 'z']]

# Eğer dosya yoksa başlıkla oluştur
if not os.path.exists(csv_path):
    pd.DataFrame(columns=columns).to_csv(csv_path, index=False)

# Streamlit UI
st.set_page_config(page_title="Finger Collector", layout="centered")
st.title("🖐 Finger Data Collector")

label = st.selectbox("Select label:", ["thumb", "index", "middle", "ring", "pinky"])
save_button = st.button("💾 Save current sample")
frame_placeholder = st.empty()

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Kamera setup
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

landmark_row = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.error("Kamera açılamadı.")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    landmark_row = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            row = []
            for lm in hand_landmarks.landmark:
                row.extend([lm.x, lm.y, lm.z])
            landmark_row = row

    # Görüntüyü göster
    frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR), channels="BGR")

    # Save'e basıldıysa ve el varsa → doğrudan CSV’ye yaz
    if save_button and landmark_row:
        new_data = pd.DataFrame([[label] + landmark_row], columns=columns)
        new_data.to_csv(csv_path, mode='a', header=False, index=False)
        st.success(f"✅ Sample saved as '{label}'")

        # Save butonunu sıfırla
        st.rerun()

cap.release()
cv2.destroyAllWindows()