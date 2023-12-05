# Splicing and Copy-Move Dataset Generator #

This code consist on 2 different dataset generators that use the TIMIT dataset and apply splicing and copy-move forgery to each audio.
The code work as follows:
- FIRST METHOD - RandomPosition:
    For each audio substract a random segment from that audio and select a random point to insert the segment in that point, then insert the rest of the original audio after the segment.
- SECOND METHOD - Concatenation (Based on the paper: 'Autoencoder for foregery detection'):
    For each audio substract segments of 2s and 1s and concatenate them in different ways so that we create for each original audio 3s and 2s forgered audios.
