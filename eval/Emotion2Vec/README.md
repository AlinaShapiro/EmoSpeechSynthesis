# Emotion2Vec
Unofficial repository, Please see the following links for mopre details:
C<sup>2</sup>SER: [Paper](https://arxiv.org/abs/2502.18186) | [Code](https://github.com/zxzhao0/C2SER) | [HuggingFace](https://huggingface.co/collections/ASLP-lab/c2ser-67bc735d820403e7969fe8a0)

## Introduction

This repository contains the implementation of Emotion2Vec, a self-supervised learning (SSL) model for speech emotion recognition, as presented in our paper "Steering Language Model to Stable Speech Emotion Recognition via Contextual Perception and Chain of Thought". 

## Requirements and Installation

This project follows the fairseq installation process.

### Requirements

- PyTorch version >= 1.10.0
- Python version >= 3.8

### Installation

To install fairseq and develop locally:

```bash
git clone https://github.com/pytorch/fairseq
cd fairseq
pip install --editable ./
```

### Feature Extraction  and Inference based on FunASR

```python
from funasr import AutoModel

model = AutoModel(model="iic/emotion2vec_plus_large")

wav_file = f"{model.model_path}/example/test.wav"
res = model.generate(wav_file, output_dir="./outputs", granularity="utterance", extract_embedding=False)
print(res)
```
