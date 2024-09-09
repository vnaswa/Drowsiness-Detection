# Drowsiness Detection System

## Overview

This project is a real-time drowsiness detection system that uses a webcam to monitor a driver's eye movements. The system detects signs of drowsiness by analyzing the eye aspect ratio (EAR) and triggers an alert if drowsiness is detected.

## Features

- **Real-Time Drowsiness Detection:** Monitors the driver's eye aspect ratio to detect drowsiness.
- **Visual Feedback:** Displays an overlay on the webcam feed indicating drowsiness status.
- **Audio Alert:** Uses text-to-speech to deliver an audible alert if drowsiness is detected.

## Prerequisites

- **Python 3.x**
- **OpenCV:** For computer vision tasks and handling webcam input.
- **dlib:** For facial landmark detection.
- **pyttsx3:** For text-to-speech functionality.
- **scipy:** For calculating Euclidean distances.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/vnaswa/drowsiness-detection.git
    cd drowsiness-detection
    ```

2. **Install Required Libraries:**

    You can install the required libraries using `pip`. Make sure you have `pip` installed:

    ```bash
    pip install opencv-python dlib pyttsx3 scipy
    ```

3. **Download the Pre-trained Model:**

    You will need the `shape_predictor_68_face_landmarks.dat` file for facial landmark detection. Download it from [dlib's model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the project directory.

## Usage

1. **Connect Your Webcam:** Ensure your webcam is connected and accessible.

2. **Run the Script:**

    ```bash
    python main.py
    ```

3. **Operation:**
    - The script will open a window displaying the webcam feed.
    - If drowsiness is detected, the system will overlay a warning message on the feed and play an audible alert.

4. **Exit:**
    - To stop the script, press the 'Esc' key or close the window.

## Troubleshooting

- **Camera Issues:** Ensure no other applications are using the camera. Try different camera indices (`0`, `1`, etc.) if the camera fails to initialize.
- **File Path Issues:** Verify the path to the `shape_predictor_68_face_landmarks.dat` file is correct and accessible.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit pull requests. Contributions, suggestions, and improvements are welcome!

