# 🎥 Face & Hand Authentication Video Player

A secure video player that requires both face and hand authentication before playing videos.

## 👨‍💻 Developer
**MD SAHADAT HOSSAIN**  
Web Developer & Data Analyst  
[Portfolio](https://developersahadat.vercel.app/) | [GitHub](https://github.com/davsahadat)

## ✨ Features

### 🔐 Dual Authentication
- **Face Detection** 👤
  - Real-time face mesh detection
  - High-accuracy facial landmarks
  - Visual mesh overlay feedback

- **Hand Tracking** ✋
  - Dual-hand detection support
  - Real-time hand landmarks
  - Visual connection feedback

### 🎬 Video Playback
- **Secure Video Access** 🎥
  - Automatic video playback after authentication
  - Default video path: `C:\Users\hp\Desktop\facevar\vid.mp4`
  - Fallback to VLC player if needed

## 🛠️ Technical Requirements

### System Requirements
- Python 3.7 or higher
- Webcam for authentication
- Windows OS (for default video player)

### Python Dependencies
```bash
opencv-python==4.8.1.78
mediapipe==0.10.21
numpy==1.26.2
```

## 🚀 Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the program:
```bash
python file_manager.py
```

## 💻 Usage Guide

### Authentication Process
1. Launch the application
2. Look at the camera
3. Show your hands in the frame
4. Wait for 2 seconds of successful detection
5. Video will play automatically! 🎉

### Authentication Feedback
- "Face Detected" - When your face is recognized
- "Hand Detected" - When your hands are visible
- "Authentication Complete!" - When both are detected
- "Please show both face and hands" - When either is missing

### Video Playback
- Automatic playback after successful authentication
- Uses system default video player
- Falls back to VLC if default player fails

## 🔒 Security Features

- **Dual Authentication** 🔐
  - Requires both face AND hands
  - 2-second verification period
  - Real-time visual feedback

- **Protected Video Access** 🛡️
  - No video access without authentication
  - Secure video path handling
  - Multiple playback options

## 🎨 Visual Feedback

The system provides clear visual feedback during authentication:
- Green face mesh overlay
- Hand landmark connections
- Status text messages
- Color-coded authentication status

## ⚙️ Code Structure

```python
class SecureFileManager:
    def __init__(self):
        # Initialize face and hand detection
        # Set up video path
        # Initialize authentication state

    def authenticate(self):
        # Handle face and hand detection
        # Provide visual feedback
        # Manage authentication state

    def play_video(self):
        # Handle video playback
        # Manage fallback options
        # Error handling

    def run(self):
        # Main program flow
        # Authentication and playback
```

## 🙏 Acknowledgments

- MediaPipe for face and hand detection
- OpenCV for computer vision
- Developed by [MD SAHADAT HOSSAIN](https://developersahadat.vercel.app/)

---

Made with ❤️ by [MD SAHADAT HOSSAIN](https://developersahadat.vercel.app/) 
