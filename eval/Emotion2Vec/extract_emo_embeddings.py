import os
import torch
import torchaudio
import numpy as np
from tqdm import tqdm
import json
from funasr import AutoModel

MODEL_ID = "emotion2vec/emotion2vec_plus_large"
INPUT_DIR = "/home/alina/outputs/exp_logs/FastPitch_ft_st_4000_lr_2e_4_batch_32_4_spkr"         
OUTPUT_DIR = "/home/alina/repos/Emotion2Vec/outputs/FastPitch_ft_st_4000_lr_2e_4_batch_32_4_spkr"
os.makedirs(OUTPUT_DIR, exist_ok=True)

model = AutoModel(model=MODEL_ID, hub="hf")

def convert_tensor_in_dict(obj):
    if isinstance(obj, dict):
        return {k: convert_tensor_in_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_tensor_in_dict(v) for v in obj]
    elif isinstance(obj, torch.Tensor):
        return obj.cpu().numpy().tolist()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj

def process_and_save(wav_path, out_path_json, out_path_npy=None):
    try:
        waveform, sr = torchaudio.load(wav_path)
        if sr != 16000:
            waveform = torchaudio.functional.resample(waveform, sr, 16000)

        result = model.generate(
            waveform, 
            OUTPUT_DIR="./outputs",
            granularity="utterance",
            extract_embedding=True,
            input_len=waveform.shape[-1]
        )

        json_data = convert_tensor_in_dict(result)
        with open(out_path_json, "w") as f:
            json.dump(json_data, f, indent=2)

        if out_path_npy is not None:
            feats = [torch.tensor(r["feats"]) for r in result]
            embedding = torch.cat(feats, dim=0).mean(dim=0).numpy()
            np.save(out_path_npy, embedding)

    except Exception as e:
        print(f"Ошибка для {wav_path}: {e}")

for fname in tqdm(os.listdir(INPUT_DIR)):
    if fname.endswith(".wav"):
        wav_path = os.path.join(INPUT_DIR, fname)
        out_json = os.path.join(OUTPUT_DIR, fname.replace(".wav", ".json"))
        out_npy = os.path.join(OUTPUT_DIR, fname.replace(".wav", ".npy"))
        process_and_save(wav_path, out_json, out_npy)
