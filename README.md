# Emotional Speech Synthesis

Course project: **"Emotional Speech Synthesis using Neural Network Models"**


## Project Description

This project explores different approaches to controlling emotional expressiveness in synthesized speech using state-of-the-art TTS models. Two main strategies were implemented and evaluated:

- **SpeechT5 (Microsoft)** – A prompt-based approach where the emotion is embedded into the text using special tags (e.g., `[EMOTION] angry`) and speaker embeddings;
- **FastPitch (NVIDIA NeMo)** – A speaker-as-emotion approach where each emotion is treated as a separate speaker, with controllable pitch and duration.

Speech quality and emotional expressiveness were evaluated using:
- **UTMOS** (naturalness/quality)
- **Emotion Similarity** (cosine similarity between emotional embeddings)
- **Recall Rate** (emotion recognition accuracy)

##  Dependencies
- Python 3.10  
- PyTorch 2.2.2 + CUDA 12.4 

## Hardware Used
- **GPU**: NVIDIA RTX 3060 (12 GB VRAM)  
- **CUDA version**: 12.4  

## Environment Setup

```bash
git clone https://github.com/your-username/emotional-speech-synthesis.git
cd emotional-speech-synthesis
pip install -r requirements.txt
```

## Results of generated speech

Results of generated speech can be accessed via [gdrive link](https://drive.google.com/drive/folders/1h_hFiDUF-91LwaCDNIos2ZzQYCKceyEI?usp=sharing).