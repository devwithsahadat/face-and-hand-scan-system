# 🎥 Secure Face & Hand Authentication System

<div style="font-family: 'Edu NSW ACT Hand', cursive; font-size: 1.2em;">
A sophisticated security system that combines face and hand detection with secure file management and video playback capabilities.
</div>

## ✨ Features

### 🔐 Authentication
- **Face Detection** 👤
  - Real-time face mesh detection
  - High-accuracy facial landmark tracking
  - Visual feedback with mesh overlay

- **Hand Tracking** ✋
  - Dual-hand detection support
  - Real-time hand landmark tracking
  - Gesture recognition capabilities

### 📁 File Management
- **Secure File Operations** 🔒
  - One-time authentication for extended access
  - Protected file storage system
  - Intuitive file management interface

- **File Operations** 📂
  - Add files with secure copying
  - Delete files with confirmation
  - List files with size information
  - Direct file opening capability

### 🎬 Video Playback
- **Secure Video Access** 🎥
  - Automatic video playback after authentication
  - Support for multiple video formats
  - Fallback playback options

## 🛠️ Technical Requirements

### System Requirements
- Python 3.7 or higher
- Webcam for face and hand detection
- Windows/Linux/MacOS support

### Python Dependencies
```bash
opencv-python==4.8.1.78
mediapipe==0.10.21
numpy==1.26.2
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/secure-auth-system.git
cd secure-auth-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the system:
```bash
python file_manager.py
```

## 💻 Usage Guide

### Authentication Process
1. Launch the application
2. Look at the camera
3. Show your hands in the frame
4. Wait for authentication (2 seconds)
5. Access granted! 🎉

### File Management
- Press `l` to list files
- Press `a` to add files
- Press `d` to delete files
- Press `o` to open files
- Press `f` to open folder
- Press `q` to quit

### Video Playback
- Automatic playback after authentication
- Video path: `C:\Users\hp\Desktop\facevar\vid.mp4`
- Supports multiple video formats

## 🔒 Security Features

- **One-Time Authentication** 🔐
  - 5-minute authentication window
  - Face and hand verification
  - Secure session management

- **Protected Operations** 🛡️
  - Secure file handling
  - Protected video access
  - Safe file deletion

## 🎨 Customization

### Font Support
The system uses the beautiful "Edu NSW ACT Hand" font for enhanced visual appeal:
- Font path: `C:\Users\hp\Desktop\facevar\EduNSWACTHandPre-VariableFont_wght.ttf`
- Customizable font weights
- Elegant typography

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- MediaPipe for face and hand detection
- OpenCV for computer vision capabilities
- Edu NSW ACT Hand font for beautiful typography

---

<div style="font-family: 'Edu NSW ACT Hand', cursive; font-size: 1.1em; text-align: center; margin-top: 2em;">
Made with ❤️ for secure authentication
</div> 
