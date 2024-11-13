import subprocess

from flask import Flask, request, jsonify, render_template
import whisper
import os
import soundfile as sf
from pydub import AudioSegment

app = Flask(__name__)

# Load Whisper model
model = whisper.load_model("base")


def convert_to_mp3(input_file):
    # Convert file using ffmpeg
    output_file = "recording.wav"
    command = f"ffmpeg -i {input_file} -y {output_file}"
    subprocess.run(command, shell=True, check=True)
    input_file = "recording.wav"
    audio = AudioSegment.from_wav(input_file)
    # Convert to MP3 format
    output_file = "converted_audio.mp3"
    audio.export(output_file, format="mp3")
    return output_file


def transcribe_audio(file_path):
    # Perform speech-to-text using Whisper
    result = model.transcribe(file_path)
    print(result)
    return result["text"]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"})

    # Save the uploaded file
    # file_path = os.path.join("uploads", file.filename)
    file_path = file.filename
    file.save(file_path)

    # Convert to MP3 if necessary
    if not file_path.endswith(".mp3"):
        file_path = convert_to_mp3(file_path)

    # Transcribe audio
    try:
        transcribed_text = transcribe_audio(file_path)
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"transcribed_text": transcribed_text})


if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)
