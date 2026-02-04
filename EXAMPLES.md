# Video Transcription Examples

## Example 1: Basic Transcription

```bash
python transcribe.py my_video.mp4
```

Output: Creates `my_video_transcription.txt` with the transcribed text

## Example 2: Custom Output File

```bash
python transcribe.py presentation.mp4 -o presentation_notes.txt
```

Output: Creates `presentation_notes.txt` with the transcribed text

## Example 3: Video in a Different Directory

```bash
python transcribe.py /path/to/videos/lecture.mp4 -o lecture_transcript.txt
```

Output: Creates `lecture_transcript.txt` in the current directory

## Sample Output

When you run the script, you'll see progress messages like:

```
Extracting audio from my_video.mp4...
Audio extracted to temp_audio.wav
Transcribing audio from temp_audio.wav...
Processing speech recognition...
Cleaned up temporary file: temp_audio.wav

Transcription saved to: my_video_transcription.txt

Transcribed text:
Hello everyone, welcome to this video presentation...
```

## Testing the Script

If you don't have the dependencies installed yet:

```bash
pip install -r requirements.txt
```

Then run the script on any video file you have available.
