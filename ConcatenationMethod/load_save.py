import os

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
def get_path(audio_filename, dataset_path):
    return os.path.join(dataset_path, audio_filename)
    
def create_original_dataset_folders():
    # Create a new folder for the original dataset
    original_dataset_path = '/home/jose/src/TFG/DatasetConcatenation/OriginalDataset'
    os.makedirs(original_dataset_path, exist_ok=True)

   # Create a new folder for the spliced dataset
    spliced_dataset_path = '/home/jose/src/TFG/DatasetConcatenation/SplicingDataset'
    os.makedirs(spliced_dataset_path, exist_ok=True)

    # Create a new folder for the copy move dataset
    copy_move_dataset_path = '/home/jose/src/TFG/DatasetConcatenation/CopyMoveDataset'
    os.makedirs(copy_move_dataset_path, exist_ok=True)

    return original_dataset_path, copy_move_dataset_path, spliced_dataset_path
