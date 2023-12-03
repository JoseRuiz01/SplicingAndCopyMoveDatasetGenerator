import os
import soundfile 

# Function to load all WAV files 
def load_audio_files(folder_path):
    audio_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".WAV"):
                file_path = os.path.join(root, file)
                audio_files.append(file_path)
    return audio_files

# Function to return the path to save the audio forgered file
def save_files(original_audio_path, iteration, dataset_path):
    audio_filename = f"{os.path.basename(original_audio_path)[:-4]}_{iteration}.wav"
    return os.path.join(dataset_path, audio_filename)
    