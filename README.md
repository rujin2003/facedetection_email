# Face Detection and Email Alert System

This Python project uses OpenCV's Haar Cascade for face detection through a webcam and sends an email alert when a face is detected. The project is integrated with a simple GUI for email authentication.

## Description

This script performs the following tasks:
1. Captures video from the webcam.
2. Detects faces in the video feed using Haar Cascade.
3. Sends an email alert when a face is detected.
4. Uses a Tkinter GUI for user email authentication.

## Features

- Real-time face detection using OpenCV.
- Sends an email alert when a face is detected.
- Simple Tkinter GUI for entering email credentials.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/face-detection-email-alert.git
    cd face-detection-email-alert
    ```

2. Install the required Python packages:

    ```bash
    pip install opencv-python smtplib tk
    ```

## Usage

1. Update the script with your email credentials in the Tkinter GUI section:

    ```python
    user_username = "your_email@gmail.com"
    user_password = "your_password"
    ```

2. Run the script:

    ```bash
    python face_detection_email_alert.py
    ```

3. Enter your email credentials in the Tkinter GUI that appears.

4. The webcam feed will start, and the script will monitor for faces. When a face is detected, an email alert will be sent.
