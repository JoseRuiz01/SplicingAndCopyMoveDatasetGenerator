import numpy as np
import librosa

# Function to apply forgery
def apply_forgery(original_audio, splice_audio):
    splice_start = np.random.randint(0, len(original_audio))
    spliced_audio = original_audio[:splice_start].copy()
    spliced_audio = np.concatenate((spliced_audio, splice_audio))
    spliced_audio = np.concatenate((spliced_audio, original_audio[splice_start + len(splice_audio):]))
    return spliced_audio

# Function to select a random segment 
def select_random_segment(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    total_duration = librosa.get_duration(y=y, sr=sr)
    
    segment_duration = np.random.uniform(1, total_duration-0.5)
    
    start_time = np.random.uniform(0, total_duration - segment_duration)
    end_time = start_time + segment_duration
    segment = y[int(start_time * sr):int(end_time * sr)]
    return segment, sr  

# Calculate the RMS (Root Mean Square) between the two segments to tell if they are different
def checkRMSDifference(audio1, audio2, umbral):
    min_length = min(len(audio1), len(audio2))
    rms_difference = np.sqrt(np.mean((audio1[:min_length] - audio2[:min_length])**2))
    return rms_difference > umbral