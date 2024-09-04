import cv2

def extract_frames(video_path, num_frames=5):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not video_capture.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return []

    frames = []
    count = 0
    
    while True:
        # Read the next frame
        ret, frame = video_capture.read()
        
        # Check if frame is successfully read
        if not ret:
            print("No more frames to read .")
            break
        
        # Save a few frames to disk (for debugging)
        if count < num_frames:
            cv2.imwrite(f'frame_{count}.jpg', frame)
            print(f"Frame {count} saved.")
        
        frames.append(frame)
        count += 1
    
    # Release the video capture object
    video_capture.release()
    
    print(f"Total frames extracted: {len(frames)}")
    return frames
