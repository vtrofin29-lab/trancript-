#!/usr/bin/env python3
"""
Video Transcription Script
This script extracts audio from a video file and transcribes it to text.
"""

import argparse
import os
import sys
import tempfile
from pathlib import Path

try:
    from moviepy.editor import VideoFileClip
    import speech_recognition as sr
except ImportError as e:
    print(f"Error: Missing required library - {e}")
    print("Please install required dependencies:")
    print("  pip install moviepy SpeechRecognition pydub")
    sys.exit(1)


def extract_audio(video_path, audio_path):
    """
    Extract audio from video file and save it as WAV.
    
    Args:
        video_path: Path to input video file
        audio_path: Path to output audio file (WAV format)
    """
    print(f"Extracting audio from {video_path}...")
    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path, verbose=False, logger=None)
        video.close()
        print(f"Audio extracted to {audio_path}")
    except Exception as e:
        print(f"Error extracting audio: {e}")
        raise


def transcribe_audio(audio_path):
    """
    Transcribe audio file to text using Google Speech Recognition.
    
    Args:
        audio_path: Path to audio file
        
    Returns:
        Transcribed text as string
    """
    print(f"Transcribing audio from {audio_path}...")
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_path) as source:
            # Record the audio data
            audio_data = recognizer.record(source)
            
            # Recognize speech using Google Speech Recognition
            print("Processing speech recognition...")
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        print("Warning: Speech recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Error: Could not request results from speech recognition service; {e}")
        raise
    except Exception as e:
        print(f"Error during transcription: {e}")
        raise


def transcribe_video(video_path, output_path=None):
    """
    Main function to transcribe video to text file.
    
    Args:
        video_path: Path to input video file
        output_path: Path to output text file (optional)
    """
    # Validate input file
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        sys.exit(1)
    
    # Set default output path if not provided
    if output_path is None:
        video_name = Path(video_path).stem
        output_path = f"{video_name}_transcription.txt"
    
    # Create temporary audio file with unique name
    temp_audio_fd, temp_audio = tempfile.mkstemp(suffix=".wav", prefix="transcript_audio_")
    os.close(temp_audio_fd)  # Close the file descriptor as we'll write with moviepy
    
    try:
        # Extract audio from video
        extract_audio(video_path, temp_audio)
        
        # Transcribe audio to text
        transcription = transcribe_audio(temp_audio)
        
        # Check if transcription is empty
        if not transcription or transcription.strip() == "":
            print("\nWarning: No speech was detected or transcription resulted in empty text.")
            print("This could be due to:")
            print("  - No speech in the video")
            print("  - Poor audio quality")
            print("  - Unsupported language")
            print("  - Background noise")
            transcription = "[No speech detected or transcription failed]"
        
        # Save transcription to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(transcription)
        
        print(f"\nTranscription saved to: {output_path}")
        print(f"\nTranscribed text:\n{transcription}")
        
    finally:
        # Clean up temporary audio file
        if os.path.exists(temp_audio):
            os.remove(temp_audio)
            print(f"\nCleaned up temporary file: {temp_audio}")


def main():
    """Command-line interface for the transcription script."""
    parser = argparse.ArgumentParser(
        description="Transcribe words from a video file to a text file"
    )
    parser.add_argument(
        "video_file",
        help="Path to the video file to transcribe"
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to output text file (default: <video_name>_transcription.txt)",
        default=None
    )
    
    args = parser.parse_args()
    
    transcribe_video(args.video_file, args.output)


if __name__ == "__main__":
    main()
