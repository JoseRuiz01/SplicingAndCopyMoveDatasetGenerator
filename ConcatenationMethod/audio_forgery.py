import numpy as np
import librosa

# Function to select a random segment 
def selectRandomSegment(audio, sr, segment_duration):
    total_duration = librosa.get_duration(y=audio, sr=sr)
    start_time = np.random.uniform(0, total_duration - segment_duration)
    end_time = start_time + segment_duration
    segment = audio[int(start_time * sr):int(end_time * sr)]
    return segment  

# Concatenate audios sent
def concatenateAudios(original_segment, forged_segment, sr, time):
    audios = []
    audios.append(np.concatenate((original_segment[:int(sr * time)], forged_segment, original_segment[int(sr * time):])))
    audios.append(np.concatenate((original_segment, forged_segment)))
    audios.append(np.concatenate((forged_segment, original_segment)))
    return  audios

# Select 1s and 2s segments of the original, concatenate them and return
def getForgeredAudios(audio, forged_segment_1, forged_segment_2, sr):
    original_segment_2sec = selectRandomSegment(audio, sr, 2)
    original_segment_1sec = selectRandomSegment(audio, sr, 1)
    audios = concatenateAudios(original_segment_2sec, forged_segment_1, sr, 1)
    audios.extend(concatenateAudios(original_segment_1sec, forged_segment_2, sr, 0.5))
    return audios

# Calculate the RMS (Root Mean Square) between the two segments to tell if they are different
def checkRMSDifference(audio1, audio2, umbral):
    min_length = min(len(audio1), len(audio2))
    rms_difference = np.sqrt(np.mean((audio1[:min_length] - audio2[:min_length])**2))
    return rms_difference > umbral

# Load a random audio file from timit_files
def getSplicingSegment(original_audio, timit_files, umbral):
    while True:
        splice_audio, sr_splice = librosa.load(np.random.choice(timit_files), sr=None)
        # check if it is different from the original audio
        if checkRMSDifference(splice_audio, original_audio, umbral): break
    return splice_audio, sr_splice

# Logic to obtain list of audios for splicing
def getD1sSegmentsForSplicing(original_audio, timit_files, umbral):
    splicing_audio1, sr_splicing1 = getSplicingSegment(original_audio, timit_files, umbral)
    splicing_audio2, sr_splicing2 = getSplicingSegment(original_audio, timit_files, umbral)
    while True:
        D1s_segment_1 = selectRandomSegment(splicing_audio1, sr_splicing1, 1)
        D1s_segment_2 = selectRandomSegment(splicing_audio2, sr_splicing2, 1)
        if checkRMSDifference(D1s_segment_1, D1s_segment_2, umbral): break
    return D1s_segment_1, D1s_segment_2

# Logic to obtain list of audios for copy-move
def getD1sSegmentsForCopyMove(original_audio, sr, umbral):
    while True:
        D1s_segment_1 = selectRandomSegment(original_audio, sr, 1)
        D1s_segment_2 = selectRandomSegment(original_audio, sr, 1)
        if checkRMSDifference(D1s_segment_1, D1s_segment_2, umbral): break
    return D1s_segment_1, D1s_segment_2
