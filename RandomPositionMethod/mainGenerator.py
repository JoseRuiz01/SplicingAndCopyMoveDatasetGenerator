import librosa
import soundfile 
import numpy as np
from audio_forgery import *
from load_save import *

# Path to the TIMIT dataset
timit_path = '/home/jose/src/TFG/TIMIT/data/lisa/data/timit/raw/TIMIT'


# Create a new folder for the spliced dataset
spliced_dataset_path = '/home/jose/src/TFG/DatasetRandomPositionMethod/SplicingDataset'
os.makedirs(spliced_dataset_path, exist_ok=True)

# Create a new folder for the copy move dataset
copy_move_dataset_path = '/home/jose/src/TFG/DatasetRandomPositionMethod/CopyMoveDataset'
os.makedirs(copy_move_dataset_path, exist_ok=True)


# Load TIMIT audio files
timit_files = load_audio_files(timit_path)


# Outer loop
for iteration in range(5):

    # Inner loop
    for original_audio_path in timit_files:

        # Load Original Audio
        original_audio, sr = librosa.load(original_audio_path, sr=None)


        # Select segments for splicing and copyMove
        while True:
            splice_audio_path = np.random.choice(timit_files)
            splice_segment, _ = select_random_segment(splice_audio_path)
            if len(splice_segment) < len(original_audio): break

        copy_move_segment, _ = select_random_segment(original_audio_path)

        # Apply forgery
        spliced_audio = apply_forgery(original_audio, splice_segment)
        copy_move_audio = apply_forgery(original_audio, copy_move_segment)


        # Save the audio
        spliced_audio_path = save_files(original_audio_path, iteration, spliced_dataset_path)
        soundfile.write(spliced_audio_path, spliced_audio, sr)
        
        copy_move_audio_path = save_files(original_audio_path, iteration, copy_move_dataset_path)
        soundfile.write(copy_move_audio_path, copy_move_audio, sr)