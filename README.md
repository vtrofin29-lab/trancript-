# trancript-

A simple video transcription tool that extracts audio from video files and converts speech to text.

## Features

- Extract audio from video files
- Transcribe speech to text using Google Speech Recognition
- Save transcription to a text file
- Support for various video formats (MP4, AVI, MOV, etc.)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/vtrofin29-lab/trancript-.git
cd trancript-
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

**Note:** You may also need to install `ffmpeg` on your system:
- **Ubuntu/Debian:** `sudo apt-get install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Usage

### Basic Usage

Transcribe a video file:
```bash
python transcribe.py path/to/your/video.mp4
```

This will create a text file named `video_transcription.txt` containing the transcribed text.

### Custom Output File

Specify a custom output file:
```bash
python transcribe.py path/to/your/video.mp4 -o my_transcription.txt
```

### Command-line Options

- `video_file`: Path to the video file to transcribe (required)
- `-o, --output`: Path to output text file (optional, default: `<video_name>_transcription.txt`)

### Example

```bash
# Transcribe a video and save to default output file
python transcribe.py my_video.mp4

# Transcribe a video and save to a specific file
python transcribe.py my_video.mp4 -o output.txt
```

## How It Works

1. The script extracts audio from the video file using MoviePy
2. The extracted audio is saved as a temporary WAV file
3. Google Speech Recognition API transcribes the audio to text
4. The transcription is saved to a text file
5. The temporary audio file is cleaned up

## Requirements

- Python 3.6+
- moviepy
- SpeechRecognition
- pydub
- ffmpeg (system dependency)

## Limitations

- Requires internet connection (uses Google Speech Recognition API)
- Best results with clear audio and minimal background noise
- Long videos may take time to process
- Audio in languages other than English may require additional configuration

## License

This project is open source and available for use.