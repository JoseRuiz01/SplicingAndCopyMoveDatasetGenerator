import librosa
import soundfile 
from audio_forgery import *
from load_save import *

# Path to the TIMIT dataset
timit_path = '/home/jose/src/TFG/TIMIT/data/lisa/data/timit/raw/TIMIT'

# Create new folders for the original, spliced and copyMove datasets
original_dataset_path, splicing_dataset_path, copy_move_dataset_path = create_original_dataset_folders()

# Load TIMIT audio files
timit_files = loadAudioFiles(timit_path)

#  umbral percentage
umbral_percentage = 1.0


# TIMIT database are segmented into audio clips with durations of 
# 1 second (1s), 2 seconds (2s), and 3 seconds (3s).
for original_audio_path in timit_files:
    original_audio, sr = librosa.load(original_audio_path, sr=None)

    # Save audio without forgery (length 3s)
    audio_path = getPath(f"{os.path.basename(original_audio_path)}", original_dataset_path)
    soundfile.write(audio_path, original_audio, sr)

    # Define the minimum umbral 
    max_amplitude = np.max(np.abs(original_audio))
    umbral = umbral_percentage / 100 * max_amplitude

    # Apply forgery
    D1s_segment_1, D1s_segment_2 = getD1sSegmentsForSplicing(original_audio, timit_files, umbral)
    splicing_audios = getForgeredAudios(original_audio, D1s_segment_1, D1s_segment_2, sr)
    D1s_segment_1, D1s_segment_2 = getD1sSegmentsForCopyMove(original_audio, sr, umbral)
    copyMove_audios = getForgeredAudios(original_audio, D1s_segment_1, D1s_segment_2, sr)

    # Get rid of the .WAV
    audio_path_without_extension, _ = os.path.splitext(os.path.basename(original_audio_path))

    # Save audios with forgery (length 3s) to folder
    for idx, audio in enumerate(copyMove_audios):
        copy_move_audio_path = getPath(f"{audio_path_without_extension}_{idx}.WAV", copy_move_dataset_path)
        soundfile.write(copy_move_audio_path, audio, sr)

    for idx, audio in enumerate(splicing_audios):
        splicing_audio_path = getPath(f"{audio_path_without_extension}_{idx}.WAV", splicing_dataset_path)
        soundfile.write(splicing_audio_path, audio, sr)

