# Speech-Recognition-OpenAI-Whisper
This is a web-based application that utilizes OpenAI's Whisper for speech-to-text conversion. The application allows users to upload audio files or record audio directly from their browser and then convert the speech in these audio files to text using the Whisper model.

![image](https://github.com/user-attachments/assets/30a84b3e-b186-4869-a60d-732802d4f7b2)

This project is a sub-project of a larger initiative aimed at simplifying and enhancing the work of health officers. The overarching goal of the larger project is to develop innovative tools and technologies that streamline healthcare processes, improve data accuracy, and enhance patient care.

### Role of This Sub-Project 

This specific sub-project focuses on leveraging speech recognition technology to assist health officers in transcribing audio recordings of patient interactions, meetings, and other relevant communications. By using OpenAI's Whisper, the application aims to: 

- **Reduce Manual Effort**: Minimize the time and effort required for manual transcription of audio recordings.

- **Improve Efficiency**: Enable health officers to quickly convert spoken words into written text, allowing them to focus more on patient care and less on administrative tasks.

- **Enhance Accessibility**: Provide a user-friendly interface for both uploading existing audio files and recording new audio directly from the browser. By integrating this speech recognition application into the larger project.

## Features 

- **Audio Upload**: Users can upload audio files in various formats (e.g., MP3, M4A, WAV) for speech recognition. 

- **Audio Recording**: Users can record audio directly from their browser using the microphone, with support for starting, stopping, and submitting the recording.

- **Speech-to-Text Conversion**: The uploaded or recorded audio is processed by OpenAI's Whisper to convert speech to text.

- **Real-time Transcription**: The application provides real-time transcription of audio files, displaying the transcribed text to the user.

## Installation 

### Prerequisites 

- Python 3.6 or higher

- `pip` (Python package installer)

- `ffmpeg` (for audio processing)

### Installing FFmpeg 

#### Linux 

You can install FFmpeg using the package manager for your distribution. 

For example: 

```bash
# For Debian/Ubuntu
sudo apt update sudo apt install ffmpeg

# For Fedora
sudo dnf install ffmpeg

# For Arch Linux
sudo pacman -S ffmpeg
```
#### Windows

Download the FFmpeg release for Windows from [FFmpeg's official website](https://www.ffmpeg.org/download.html)


- Extract the downloaded zip file to a desired location (e.g., C:\ffmpeg).

- Add the FFmpeg bin directory to your system PATH:

- Open System Properties -> Advanced -> Environment Variables.

- Under System variables, find the Path variable and click Edit.

- Click New and add the path to the FFmpeg bin directory (e.g., C:\ffmpeg\bin).

- Click OK to close all dialog boxes.

#### macOS

You can install FFmpeg using Homebrew:

```bash
brew update
brew install ffmpeg
```

## Setting Up the Application

### Clone the Repository:

```bash
git clone https://github.com/NjorogeMaurice/Speech-Recognition-OpenAI-Whisper.git
cd Speech-Recognition-OpenAI-Whisper
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Or

```bash
python -m flask run
```

Open your web browser and go to http://127.0.0.1:5000/ to use the application.

### Contributing

Feel free to contribute to this project by opening an issue or submitting a pull request. Contributions are welcome!







