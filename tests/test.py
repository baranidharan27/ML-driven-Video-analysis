
import unittest
from src.data_processing import extract_frames

class TestDataProcessing(unittest.TestCase):
    def test_extract_frames(self):
        video_path = 'data/sample1.mp4'  # Use a test video file here
        frames = extract_frames(video_path)
        self.assertGreater(len(frames), 0, "No frames extracted.")
        
if __name__ == "__main__":
    unittest.main()
