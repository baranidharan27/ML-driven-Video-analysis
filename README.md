# Automated Video Meeting Analysis

## Project Overview

The Automated Video Meeting Analysis project aims to develop a real-time system for analyzing video meetings using machine learning. The system focuses on detecting anomalies, analyzing emotions and behaviors, and generating insightful reports. It leverages open-source tools and technologies to provide an efficient solution for monitoring and improving meeting interactions.

## Tech Stack

- **Programming Language:** Python
- **Video Processing:** OpenCV
- **Face Detection and Recognition:** Dlib (pre-trained models)
- **Emotion Detection:** Custom machine learning models (multilingual support)
- **Web Framework:** Flask
- **Database:** SQLite
- **Development Environment:** Google Colab
- **Version Control:** GitHub

## Project Components

1. **Real-time Video Processing**
   - Captures and processes video streams in real-time.

2. **Face Detection and Recognition**
   - Utilizes pre-trained models to detect and recognize faces.

3. **Emotion Detection**
   - Analyzes facial expressions to detect emotions with multilingual support.

4. **Feature Extraction and Clustering**
   - Extracts relevant features from video frames and performs clustering.

5. **Statistical and Graphical Analysis**
   - Analyzes data statistically and visualizes results using graphs.

6. **Automated Reporting and Dashboard**
   - Generates reports and provides a dashboard for real-time analytics and alerts.

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/baranidharan27/video-meeting-analysis.git
   cd video-meeting-analysis
2 . **Install Dependencies**
Ensure you have Python 3.x installed. Install the required libraries using:

```bash

pip install -r requirements.txt
```

3. **Start the application using:**

```bash
python src/app.py
```

4. **Testing**
Unit tests are located in the test directory. Run the tests using:

```bash
 python -m unittest discover -s tests
 ```

5. **Contributing**
If you'd like to contribute to this project, please follow these steps:

-Fork the repository.

-Create a feature branch (git checkout -b feature-branch).

-Commit your changes (git commit -am 'Add new feature').

-Push to the branch (git push origin feature-branch).

-Create a new Pull Request.
