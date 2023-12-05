import numpy as np
import librosa

# Function to select a random segment 
def selectRandomSegment(audio, sr, segment_duration):
    total_duration = librosa.get_duration(y=audio, sr=sr)

    start_time = np.random.uniform(0, total_duration - segment_duration)
    end_time = start_time + segment_duration
    segment = audio[int(start_time * sr):int(end_time * sr)]
    return segment  

def concatenateAudios(original_segment, forged_segment, sr, time):
    # Save audios concatenated
    audios = []
    audios.append(np.concatenate((original_segment[:int(sr * time)], forged_segment, original_segment[int(sr * time):])))
    audios.append(np.concatenate((original_segment, forged_segment)))
    audios.append(np.concatenate((forged_segment, original_segment)))
    return  audios

def getForgeredAudios(audio, forged_segment_1, forged_segment_2, sr):
    original_segment_2sec = selectRandomSegment(audio, sr, 2)
    original_segment_1sec = selectRandomSegment(audio, sr, 1)
    audios = concatenateAudios(original_segment_2sec, forged_segment_1, sr, 1)
    audios.extend(concatenateAudios(original_segment_1sec, forged_segment_2, sr, 0.5))
    return audios

def checkRMSDifference(audio1, audio2, umbral):
    # Calculate the RMS (Root Mean Square) between the two segments to tell if they are different
    min_length = min(len(audio1), len(audio2))
    rms_difference = np.sqrt(np.mean((audio1[:min_length] - audio2[:min_length])**2))
    return rms_difference > umbral


def getSplicingSegment(original_audio, timit_files, umbral):
    while True:
        # Load a random audio file from timit_files
        splice_audio, sr_splice = librosa.load(np.random.choice(timit_files), sr=None)
        # Length of splice_audio matches the length of original_audio
        if checkRMSDifference(splice_audio, original_audio, umbral): break
    return splice_audio, sr_splice


def getD1sSegmentsForSplicing(original_audio, timit_files, umbral):
    splicing_audio1, sr_splicing1 = getSplicingSegment(original_audio, timit_files, umbral)
    splicing_audio2, sr_splicing2 = getSplicingSegment(original_audio, timit_files, umbral)
    while True:
        D1s_segment_1 = selectRandomSegment(splicing_audio1, sr_splicing1, 1)
        D1s_segment_2 = selectRandomSegment(splicing_audio2, sr_splicing2, 1)
        if checkRMSDifference(D1s_segment_1, D1s_segment_2, umbral): break
    return D1s_segment_1, D1s_segment_2


def getD1sSegmentsForCopyMove(original_audio, sr, umbral):
    while True:
        D1s_segment_1 = selectRandomSegment(original_audio, sr, 1)
        D1s_segment_2 = selectRandomSegment(original_audio, sr, 1)
        if checkRMSDifference(D1s_segment_1, D1s_segment_2, umbral): break
    return D1s_segment_1, D1s_segment_2
