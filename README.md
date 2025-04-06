# 🖐 FingerIdentifierAI

This project allows real-time hand landmark detection and labeling using **MediaPipe**, **OpenCV**, and **Streamlit**.  
It helps collect finger data for training machine learning models that can later recognize hand/finger positions.

---

## Features
- Real-time webcam hand tracking
- Landmark extraction (21 points × x, y, z)
- Easy labeling (thumb, index, middle, ring, pinky)
- Export to `CSV` for ML training

---

## 🚀 Run the app

```bash
pip install -r requirements.txt
streamlit run app.py

## 📂 Output

The app generates a file called `finger_data.csv`, whichj contains labeled hand landmark data.

Each row in this file represents a captured hand pose, consisting of:
- A `label` (e.g., "thumb", "index", etc.)
- 63 values representing the x, y, z coordinates of 21 hand landmarks

### ⚠️ Why `finger_data.csv` is NOT inmcluded

This file is **not included in the repository** because it contains **personally collected hand pose data** — in other words, **it's literally my own hand**.  
Since it qualifies as **biometric data**, sharing it publicly could raise privacy or ethical concerns (e.g. GDPR / KVKK compliance).

If you want to test the project, you can run the app yourself and create your own dataset easily.
