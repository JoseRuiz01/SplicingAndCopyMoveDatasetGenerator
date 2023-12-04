import librosa
import soundfile 
from audio_forgery import *
from load_save import *

# Path to the TIMIT dataset
timit_path = '/home/jose/src/TFG/TIMIT/data/lisa/data/timit/raw/TIMIT'

# Create new folders for the original, spliced and copyMove datasets
original_dataset_path, splicing_dataset_path, copy_move_dataset_path = create_original_dataset_folders()

# Load TIMIT audio files
timit_files = load_audio_files(timit_path)

# TIMIT database are segmented into audio clips with durations of 
# 1 second (1s), 2 seconds (2s), and 3 seconds (3s).
for original_audio_path in timit_files:
    copyMove_audios = []
    splicing_audios = []
    original_audio, sr = librosa.load(original_audio_path, sr=None)

    # Save audio without forgery (length 3s)
    D3s_segment = select_random_segment(original_audio, sr, 3)
    D3s_segment_path = get_path(f"{os.path.basename(original_audio_path)}", original_dataset_path)
    soundfile.write(D3s_segment_path, D3s_segment, sr)

    # Define the minimum umbral 
    max_amplitude = np.max(np.abs(original_audio))
    umbral = umbral_porcentaje / 100 * max_amplitude

    while True:
        # Load a random audio file from timit_files
        splice_audio, sr_splice = librosa.load(np.random.choice(timit_files), sr=None)

        # Length of splice_audio matches the length of original_audio
        min_length = min(len(original_audio), len(splice_audio))
        original_audio_trimmed = original_audio[:min_length]
        splice_audio_trimmed = splice_audio[:min_length]

        # Calculate the RMS (Root Mean Square) between the two segments to tell if they are different
        rms_difference = np.sqrt(np.mean((splice_audio_trimmed - original_audio_trimmed)**2))

        if rms_difference > umbral: break
    
    # Apply forgery
    copyMove_audios = get_forgered_audios(original_audio, original_audio, umbral, sr, sr)
    splicing_audios = get_forgered_audios(original_audio, splice_audio, umbral, sr, sr_splice)

   
    # Save audios with forgery (length 3s)
    for audio in copyMove_audios:
        copy_move_audio_path = get_path(f"{os.path.basename(original_audio_path)}{copyMove_audios.index()}.wav", copy_move_dataset_path)
        soundfile.write(copy_move_audio_path, audio, sr)

    for audio in splicing_audios:
        splicing_audio_path = get_path(f"{os.path.basename(original_audio_path)}{splicing_audios.index()}.wav", splicing_dataset_path)
        soundfile.write(splicing_audio_path, audio, sr)

