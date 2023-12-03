#########################################
# Splicing and Copy-Move Data Generator #
#########################################

This code consist on a dataset generator that uses the TIMIT dataset and apply splicing and copy-move forgery to each audio.
The code work as follows:
- Iterate through each audio file from the TIMIT dataset.
    - For splicing: Select a random audio from the same dataset.
    - For Splicing: Substract a random segment from that audio.
    
    - For Copy-move: subtract a random segment from the same original audio.

- Select a random point in the original audio.
- Insert the segment in that point in the original audio.
- Insert the rest of the original audio after the segment.
- Return the forgered audio and save it in to the folders dataset
