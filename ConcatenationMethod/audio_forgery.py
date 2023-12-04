import numpy as np
import librosa

umbral_porcentaje = 1.0

# Function to select a random segment 
def select_random_segment(audio, sr, segment_duration):
    total_duration = librosa.get_duration(y=audio, sr=sr)

    start_time = np.random.uniform(0, total_duration - segment_duration)
    end_time = start_time + segment_duration
    segment = audio[int(start_time * sr):int(end_time * sr)]
    return segment  

def concatenateAudios(D2s_segment, D1s_segment):
    audios = []
    audios.append(np.concatenate((D2s_segment[:1], D1s_segment, D2s_segment[1:])))
    audios.append(np.concatenate((D2s_segment, D1s_segment)))
    audios.append(np.concatenate((D1s_segment, D2s_segment)))
    return  audios

def get_forgered_audios(audio1, audio2, umbral, sr1, sr2):
    # Define the minimum umbral 
    forgered_audios = []
    D2s_segment = select_random_segment(audio1, sr1, 2)

    while True:
        D1s_segment_1 = select_random_segment(audio2, sr2, 1)
        D1s_segment_2 = select_random_segment(audio2, sr2, 1)
        # Calculate the RMS (Root Mean Square) between the two segments to tell if they are different
        rms_difference = np.sqrt(np.mean((D1s_segment_1 - D1s_segment_2)**2))
        # CHeck if the RMS (Root Mean Square) is greater than the defined umbral (1%)
        if rms_difference > umbral: break

    forgered_audios = concatenateAudios(D2s_segment, D1s_segment_1)
    forgered_audios.extend(concatenateAudios(D2s_segment, D1s_segment_2))

    return forgered_audios

