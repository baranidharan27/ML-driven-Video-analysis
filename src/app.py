import sys
import os
import cv2
from fer import FER

# Add the parent directory of src to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import load_face_detector, detect_faces

def process_video(video_path):
    # Load the face detector
    face_cascade = load_face_detector()
    # Load the emotion detector
    emotion_detector = FER()

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return
    
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect faces in the frame
        faces = detect_faces(frame, face_cascade)
        
        # Analyze emotions
        emotions = emotion_detector.detect_emotions(frame)

        # Draw rectangles around detected faces and annotate emotions
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Draw detected emotions on the frame
            for emotion in emotions:
                cv2.putText(frame, f"{emotion['emotions']}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Save or display the frame
        output_frame_path = f"frame_{frame_count}.jpg"
        cv2.imwrite(output_frame_path, frame)
        print(f"Processed frame {frame_count}, faces detected: {len(faces)}, emotions: {emotions}")
        
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'data/sample1.mp4'  # Update with your video path
    process_video(video_path)
