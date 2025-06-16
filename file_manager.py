import cv2
import mediapipe as mp
import numpy as np
import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class SecureFileManager:
    def __init__(self):
        # Initialize MediaPipe solutions
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        # Initialize face detection
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Initialize hand tracking
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        
        # Video path
        self.video_path = r"C:\Users\hp\Desktop\facevar\vid.mp4"
        
        # Authentication state
        self.is_authenticated = False
        self.auth_timeout = 300  # 5 minutes timeout
        self.last_auth_time = None
        
        # Initialize Tkinter root
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window
        
    def authenticate(self):
        print("Please look at the camera and show your hands for authentication...")
        auth_start_time = datetime.now()
        face_detected = False
        hand_detected = False
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                return False
                
            # Convert the BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Process face detection
            face_results = self.face_mesh.process(rgb_frame)
            
            # Process hand tracking
            hand_results = self.hands.process(rgb_frame)
            
            # Check face detection
            if face_results.multi_face_landmarks:
                face_detected = True
                for face_landmarks in face_results.multi_face_landmarks:
                    self.mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=face_landmarks,
                        connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_tesselation_style()
                    )
                    
                    # Add face detection text
                    cv2.putText(
                        frame,
                        "Face Detected",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2
                    )
            
            # Check hand detection
            if hand_results.multi_hand_landmarks:
                hand_detected = True
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    # Add hand detection text
                    cv2.putText(
                        frame,
                        "Hand Detected",
                        (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2
                    )
            
            # Add authentication status
            if face_detected and hand_detected:
                cv2.putText(
                    frame,
                    "Authentication Complete!",
                    (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )
                
                # Check if both face and hand have been detected for 2 seconds
                time_diff = (datetime.now() - auth_start_time).total_seconds()
                if time_diff >= 2:
                    self.is_authenticated = True
                    self.last_auth_time = datetime.now()
                    return True
            else:
                cv2.putText(
                    frame,
                    "Please show both face and hands",
                    (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    2
                )
            
            # Display the frame
            cv2.imshow('Authentication', frame)
            
            # Break if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return False
    
    def play_video(self):
        if not os.path.exists(self.video_path):
            print(f"Error: Video file not found at {self.video_path}")
            return
            
        try:
            # Try to play the video using the default system player
            os.startfile(self.video_path)
            print("Video playback started!")
        except Exception as e:
            print(f"Error playing video: {str(e)}")
            # Fallback method using VLC if available
            try:
                subprocess.run(['vlc', self.video_path])
            except:
                print("Could not play video. Please check if the video file exists and is playable.")
    
    def run(self):
        try:
            # First authenticate
            if not self.authenticate():
                print("Authentication failed!")
                return
                
            print("\nAuthentication successful!")
            cv2.destroyAllWindows()
            
            # Play the video
            self.play_video()
                    
        finally:
            # Clean up
            self.cap.release()
            cv2.destroyAllWindows()
            self.face_mesh.close()
            self.hands.close()
            self.root.destroy()

if __name__ == "__main__":
    print("Secure Video Player Started!")
    print("You will need to authenticate with your face and hands first.")
    print("Please look at the camera and show your hands when prompted.")
    
    manager = SecureFileManager()
    manager.run()