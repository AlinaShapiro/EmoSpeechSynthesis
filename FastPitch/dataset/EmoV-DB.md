# EmoV-DB Dataset Placeholder

⚠️ **The dataset is not included in this repository due to size or licensing restrictions.**

## Where to get the dataset

1. **[Recommended]** Download the preprocessed dataset from [Google Drive](https://drive.google.com/file/d/1A6452LuxJcS-P9vys2Di4_j5XFVWhbDI/view?usp=sharing)

2. Alternatively, you can download the raw EmoV-DB dataset from the [EmoV-DB GitHub page](https://github.com/numediart/EmoV-DB).  
   However, you will need to preprocess it yourself according to the instructions provided there.

   After alignment, make sure to normalize the audio files to:
   - 22 kHz sample rate  
   - Mono channel  
   - 16-bit WAV format

Please place the dataset manually in this folder. 

## Expected Structure
```
EmoV-DB_sr22/
┣ 1/
┃ ┣ amused/
┃ ┃ ┗ audio/
┃ ┣ anger/
┃ ┃ ┗ audio/
┃ ┣ disgust/
┃ ┃ ┗ audio/
┃ ┣ neutral/
┃ ┃ ┗ audio/
┃ ┣ sleepiness/
┃ ┃ ┗ audio/
┣ 2/
┃ ┣ amused/
┃ ┃ ┗ audio/
┃ ┣ anger/
┃ ┃ ┗ audio/
┃ ┣ disgust/
┃ ┃ ┗ audio/
┃ ┣ neutral/
┃ ┃ ┗ audio/
┃ ┣ sleepiness/
┃ ┃ ┗ audio/
┃ ┗ sup_data/
┣ train_manifest.json
┗ val_manifest.json
```
