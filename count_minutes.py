import os
import wave
import sys


def get_wav_duration(filename):
    with wave.open(filename, "r") as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration


def get_total_duration(folder_path):
    total_duration = 0.0
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            filepath = os.path.join(folder_path, filename)
            duration = get_wav_duration(filepath)
            total_duration += duration
    return total_duration


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path_to_your_folder")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("The provided path is not a valid directory.")
        sys.exit(1)

    total_seconds = get_total_duration(folder_path)
    total_minutes = total_seconds / 60 / 60

    print(f"Total duration: {total_minutes:.2f} hours")
