# Text2Speech_Speech2Text
# Speech to Text and Text to Speech Web Application

This is a web application that provides speech-to-text (STT) and text-to-speech (TTS) functionalities. The backend is built using Flask and the frontend allows users to upload audio files for speech-to-text conversion and enter text for text-to-speech conversion with selectable voices.

## Features

- **Speech to Text**: Upload an audio file to convert speech to text using Google Speech Recognition.
- **Text to Speech**: Enter text to convert to speech using `pyttsx3` with options for different voices (male and female).

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `ffmpeg` (for audio processing)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/speech-to-text-tts-app.git
    cd speech-to-text-tts-app
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install `ffmpeg`**:
    - Download `ffmpeg` from [FFmpeg official site](https://ffmpeg.org/download.html).
    - Follow the instructions to add `ffmpeg` to your system's PATH.

## Usage

1. **Run the Flask Application**:
    ```bash
    python app.py
    ```

2. **Open Your Browser**:
    - Navigate to `http://127.0.0.1:5000/`.

3. **Using the Application**:
    - **Speech to Text**: Upload an audio file and click "Convert" to get the text.
    - **Text to Speech**: Enter text, select a voice (male or female), and click "Convert" to download the generated speech audio.

by Shoaib Hayat @DEVPY
