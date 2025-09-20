import cv2
import mediapipe as mp
import numpy as np
import pandas as pd

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Define column names (Gesture + 21 landmarks * (x, y, z))
columns = ["gesture"] + [f"x{i}" for i in range(21)] + [f"y{i}" for i in range(21)] + [f"z{i}" for i in range(21)]

# Load existing CSV or create new DataFrame
csv_filename = "gestures.csv"
try:
    df = pd.read_csv(csv_filename)
    if df.empty:
        df = pd.DataFrame(columns=columns)
except FileNotFoundError:
    df = pd.DataFrame(columns=columns)

# Function to calculate Euclidean distance
def calculate_distance(point1, point2):
    return np.linalg.norm(np.array([point1.x - point2.x, point1.y - point2.y, point1.z - point2.z]))

# Function to normalize hand landmarks
def normalize_landmarks(landmarks):
    wrist = landmarks[0]  
    middle_base = landmarks[9]  
    scale = calculate_distance(wrist, middle_base)
    
    if scale == 0:
        return None

    normalized = []
    for lm in landmarks:
        normalized.append([(lm.x - wrist.x) / scale, (lm.y - wrist.y) / scale, (lm.z - wrist.z) / scale])
    
    return normalized

# Function to extract hand landmarks
def get_landmarks_as_row(landmarks):
    normalized_landmarks = normalize_landmarks(landmarks)
    return [coord for lm in normalized_landmarks for coord in lm] if normalized_landmarks else None

# Start video capture
cap = cv2.VideoCapture(0)
gesture_name = input("Enter gesture name: ").strip()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Gesture Capture", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                row = get_landmarks_as_row(hand_landmarks.landmark)
                if row:
                    row.insert(0, gesture_name)
                    df.loc[len(df)] = row
                    print(f"✅ Gesture '{gesture_name}' saved.")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save to CSV
df.to_csv(csv_filename, index=False)
print(f"📂 Data saved to {csv_filename}")