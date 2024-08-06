import os
import glob
import subprocess

# Define paths
wildcard_path = "/home/mark/Downloads/Jelly Roll - *"
transcription_file = "/home/mark/Downloads/transcriptions.txt"

# Find all files matching the wildcard path
files = glob.glob(wildcard_path)

# Clear the transcription file
with open(transcription_file, "w") as f:
    f.write("")

# Process each file
for file_path in files:
    try:
        # Run Whisper on the file to detect language and transcribe
        result = subprocess.run(
            ["whisper", file_path, "--language", "en"], capture_output=True, text=True
        )
        transcription = (
            result.stdout.strip()
        )  # Assuming Whisper outputs the transcription to stdout

        # Extract only the necessary transcription parts
        lines = transcription.split("\n")
        cleaned_transcription = ""
        for line in lines:
            if "-->" in line:
                parts = line.split("]")
                if len(parts) > 1:
                    cleaned_transcription += parts[1].strip() + " "

        # Append the cleaned transcription to the file
        with open(transcription_file, "a") as f:
            f.write(
                cleaned_transcription.strip() + " "
            )  # Add a space between transcriptions of different files
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
