from flask import Flask, request, render_template, send_file
import speech_recognition as sr
import os
from pydub import AudioSegment
import time
import pyttsx3

app = Flask(__name__)

@app.route('/')
def index():
    print("Index page accessed")
    return render_template('index.html')

@app.route('/speech_to_text', methods=['POST'])
def speech_to_text():
    print("Speech to Text endpoint hit")
    if 'audio' not in request.files:
        return "No file part", 400
    
    audio_file = request.files['audio']

    # Save the uploaded file
    audio_path = os.path.join('uploads', 'temp_audio')
    audio_file.save(audio_path)

    try:
        # Convert audio to WAV format
        sound = AudioSegment.from_file(audio_path)
        wav_path = audio_path + '.wav'
        sound.export(wav_path, format='wav')

        recognizer = sr.Recognizer()

        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio)
                print("Speech to text conversion successful")
                return text, 200
            except sr.RequestError:
                return "API unavailable", 500
            except sr.UnknownValueError:
                return "Unable to recognize speech", 400
    finally:
        # Ensure that temporary files are deleted
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    print("Text to Speech endpoint hit")
    text = request.form.get('text')
    voice_id = request.form.get('voice_id', 'default')

    if not text:
        return "Text is required", 400

    # Generate a unique filename using a timestamp
    filename = f"output_{int(time.time())}.mp3"

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if voice_id == 'female':
        engine.setProperty('voice', voices[1].id)  # Select female voice
    else:
        engine.setProperty('voice', voices[0].id)  # Select male voice by default

    engine.save_to_file(text, filename)
    engine.runAndWait()

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(filename)
    wav_filename = filename.replace('.mp3', '.wav')
    sound.export(wav_filename, format="wav")
    
    print("Text to speech conversion successful")
    return send_file(wav_filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    print("Starting Flask server")
    app.run(debug=True)
