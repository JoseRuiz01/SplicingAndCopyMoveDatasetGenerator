import os
import librosa
import soundfile 
import numpy as np

# Path to the TIMIT dataset
timit_path = '/home/jose/src/TIMIT/data/lisa/data/timit/raw/TIMIT/TEST'

# Function to load all WAV files 
def load_audio_files(folder_path):
    audio_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".WAV"):
                file_path = os.path.join(root, file)
                audio_files.append(file_path)
    return audio_files


# Function to select a random segment 
def select_random_segment(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    total_duration = librosa.get_duration(y=y, sr=sr)
    
    segment_duration = np.random.uniform(0.3, total_duration-0.3)
    
    start_time = np.random.uniform(0, total_duration - segment_duration)
    end_time = start_time + segment_duration
    segment = y[int(start_time * sr):int(end_time * sr)]
    return segment, sr  

# Function to apply splicing forgery
def apply_splicing(original_audio, splice_audio):
    splice_start = np.random.randint(0, len(original_audio) - len(splice_audio))
    spliced_audio = original_audio.copy()
    spliced_audio[splice_start:splice_start + len(splice_audio)] = splice_audio
    return spliced_audio


# Create a new folder for the spliced dataset
spliced_dataset_path = '/home/jose/src/SplicingDataset'
os.makedirs(spliced_dataset_path, exist_ok=True)


# Load TIMIT audio files
timit_files = load_audio_files(timit_path)

# Outer loop to iterate 5 times
for iteration in range(5):
    # Inner loop to iterate through TIMIT files
    for original_audio_path in timit_files:
        original_audio, sr = librosa.load(original_audio_path, sr=None)

        # Select a random segment from another TIMIT file
        splice_audio_path = np.random.choice(timit_files)
        splice_audio, _ = select_random_segment(splice_audio_path)

        # Ensure that the length of splice_audio is less than original_audio
        splice_len = len(splice_audio)
        while splice_len >= len(original_audio):
            splice_audio_path = np.random.choice(timit_files)
            splice_audio, _ = select_random_segment(splice_audio_path)
            splice_len = len(splice_audio)

        # Apply splicing forgery
        spliced_audio = apply_splicing(original_audio, splice_audio)

        # Save the spliced audio with a unique name
        spliced_audio_filename = f"{os.path.basename(original_audio_path)[:-4]}_{iteration}.wav"
        spliced_audio_path = os.path.join(spliced_dataset_path, spliced_audio_filename)
        soundfile.write(spliced_audio_path, spliced_audio, sr)