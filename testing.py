import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import pyttsx3

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Load gesture dataset
csv_filename = "gestures.csv"
df = pd.read_csv(csv_filename) if csv_filename else None

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

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

# Function to find closest matching gesture
def find_closest_gesture(landmarks):
    if df is None or df.empty:
        return "No gestures found in dataset."

    input_row = np.array(get_landmarks_as_row(landmarks))
    if input_row is None:
        return "Invalid landmarks."

    best_match = None
    min_distance = float('inf')

    for _, row in df.iterrows():
        stored_row = np.array(row[1:].values, dtype=np.float32)
        distance = np.linalg.norm(input_row - stored_row)
        if distance < min_distance:
            min_distance = distance
            best_match = row["gesture"]

    return best_match if best_match else "Unknown Gesture"

# Start video capture
cap = cv2.VideoCapture(0)
prev_gesture = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gesture = find_closest_gesture(hand_landmarks.landmark)

            # Display gesture text
            cv2.putText(frame, f"Gesture: {gesture}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Speak only if a new gesture is detected
            if gesture != prev_gesture:
                print(f"Recognized: {gesture}")
                engine.say(gesture)
                engine.runAndWait()
                prev_gesture = gesture

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()