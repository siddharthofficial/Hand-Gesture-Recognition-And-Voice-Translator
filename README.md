# ✋ Real-Time Hand Gesture Recognition & Voice Translator  

This project transforms a **Raspberry Pi 5** into a powerful, real-time sign language and gesture recognition device.  
It uses a Pi Camera to interpret hand movements, translates them into words, and speaks them aloud using a text-to-speech engine.  

The system features a **custom OLED display** for visual feedback, including an engaging startup animation and live transcription of recognized gestures.  

Built on **MediaPipe** for high-fidelity hand landmark detection, with a **custom-trained dataset** for accurate gesture classification.  

---

## 🚀 Core Features  

- **Real-Time Gesture Recognition** → Instantly detects and classifies hand gestures from a live camera feed.  
- **Voice Feedback** → Translates recognized gestures into spoken words using a text-to-speech engine.  
- **OLED Display Interface** →  
  - "TARANG" startup sequence  
  - Dynamic progress bar  
  - Animated *system ready* indicator  
  - Live transcription of recognized gestures  
- **Custom Gesture Training** → Train & add your own gestures with ease.  
- **Low Latency** → Optimized for Raspberry Pi 5 for smooth performance.  
- **Optional Camera View** → Press **`a`** to toggle a debugging camera feed with landmark overlays.  

---

## 🛠️ Hardware Requirements  

- **Raspberry Pi 5** (Recommended for best performance)  
- **Raspberry Pi Camera Module** (v2 or v3 recommended)  
- **SSD1306 OLED Display** (128x32 pixels, I²C)  
- **Speakers / Headphones** (connected to Pi’s audio output)  

---

## 💻 Software Requirements  

- **Python 3**  
- Required libraries:  
  - `opencv-python` → Camera feed processing  
  - `mediapipe` → Hand tracking & landmark detection  
  - `pandas`, `numpy` → Data handling & calculations  
  - `luma.oled` → OLED display control  
  - `pyttsx3` → Text-to-speech  
  - `picamera2` → Pi Camera interface  

📌 Install dependencies from `requirements.txt`.  

---

## ⚙️ Setup & Installation  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/siddharthofficial/Hand-Gesture-Recognition-And-Voice-Translator.git
   cd Hand-Gesture-Recognition-And-Voice-Translator
   
2. **Enable Interfaces on Raspberry Pi**  
   ```bash
   sudo raspi-config

  Go to Interface Options → Enable I²C & Camera.
  Reboot your Pi after enabling.

3. **Install Dependencies (recommended inside a virtual environment)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

4. **Install additional package for TTS:**
   ```bash
    sudo apt-get install espeak-ng
   
5. **Download MediaPipe Model**

     Download hand_landmarker.task from Google for Developers
     Place it inside the project’s root directory.


## 🤝 Contributing

Pull requests are welcome! If you’d like to improve gesture classification, add multi-language support, feel free to fork and submit PRs.


## 📬 Contact Us

If you have any questions, suggestions, or collaboration ideas, feel free to reach out:  


- 👤 **Name**: Rohan Raj
- 📧 **Email**: curiousrohan99977@gmail.com
- 💼 **LinkedIn**: [https://www.linkedin.com/in/rohan-raj-67771b259/](https://www.linkedin.com/in/rohan-raj-67771b259/)  

- 👤 **Name**: Siddharth Jain  
- 📧 **Email**: jainsid077@gmail.com 
- 💼 **LinkedIn**: [https://www.linkedin.com/in/siddharth-jain-979a35253/](https://www.linkedin.com/in/siddharth-jain-979a35253/)  









