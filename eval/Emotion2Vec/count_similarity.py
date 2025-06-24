import os
import numpy as np
from glob import glob
from scipy.spatial.distance import cosine
import json
from collections import defaultdict

GT_DIR = "/home/alina/repos/EmoSpeechSynthesis/eval/Emotion2Vec/outputs/GT_EMOV-DB"
PRED_DIR = "/home/alina/repos/EmoSpeechSynthesis/eval/Emotion2Vec/outputs/FastPitch_ft_st_4000_lr_2e_4_batch_32_4_spkr"

emotion_sims = defaultdict(list)

results = []

for gt_path in glob(f"{GT_DIR}/*.json"):
    fname = os.path.basename(gt_path)
    pred_path = os.path.join(PRED_DIR, fname)
    
    if not os.path.exists(pred_path) and not os.path.exists(f"{pred_path.replace('.json', '_gen.json')}"):
        print(f"Missing: {pred_path}")
        continue

    with open(gt_path, "r") as f:
        gt_emb = json.load(f)

    with open(f"{pred_path.replace('.json', '_gen.json')}", "r") as f:
        pred_emb = json.load(f)

    gt_emb = gt_emb[0]["feats"]
    pred_emb = pred_emb[0]["feats"]

    sim = 1 - cosine(gt_emb, pred_emb)
    results.append((fname, sim))

    emotion = fname.split("_")[0]
    emotion_sims[emotion].append(sim)

for fname, sim in results:
    print(f"{fname}: cosine similarity = {sim:.4f}")

avg_sim = np.mean([sim for _, sim in results])
print(f"\nOverall average cosine similarity: {avg_sim:.4f}")

print("\nAverage cosine similarity by emotion:")
for emotion, sims in sorted(emotion_sims.items()):
    mean_sim = np.mean(sims)
    print(f"  {emotion}: {mean_sim:.4f}")