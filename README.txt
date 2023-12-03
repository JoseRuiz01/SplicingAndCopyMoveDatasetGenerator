# Splicing Data Generator #

This code consist on a dataset generator that uses the TIMIT dataset and apply splicing forgery to each audio.
The code work as follows:
- Iterate through each audio file from the TIMIT dataset.
- Select a random audio from the same dataset.
- Substract a random segment from that audio.
- Select a random point in the original audio.
- Insert the segment in that point in the original audio.
- Insert the rest of the original audi after the segment.
- Return the spliced audio and save it in to the folder 'SplicingDataset' 